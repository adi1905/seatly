from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "ticketflow"
    environment: str = "dev"
    log_level: str = "INFO"

    database_url: str = "postgresql+asyncpg://ticketflow:ticketflow@localhost:5433/ticketflow"
    redis_url: str = "redis://localhost:6380/0"
    rabbitmq_url: str = "amqp://ticketflow:ticketflow@localhost:5672//"
    smtp_host: str = "localhost"
    smtp_port: int = 1025


settings = Settings()
