from drivers.api_driver import api_driver_impl
from loguru import logger


@logger.catch
def main():
    """Application entry point."""
    logger.info("Starting application.")
    api_driver_impl.run()


if __name__ == "__main__":
    main()
