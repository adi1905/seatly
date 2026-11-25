import httpx
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from app.main import app


async def test_healthz() -> None:
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    assert "x-request-id" in response.headers


async def test_migrations_install_extensions(postgres_url: str) -> None:
    engine = create_async_engine(postgres_url)
    async with engine.connect() as conn:
        rows = (await conn.execute(text("SELECT extname FROM pg_extension"))).scalars().all()
    await engine.dispose()
    assert "citext" in rows
    assert "pg_trgm" in rows
