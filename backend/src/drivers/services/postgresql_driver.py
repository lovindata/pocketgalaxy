import psycopg2
from adapters.routes.connections.dto import MySqlInfoIDto
from psycopg2 import OperationalError


class PostgreSqlDriver:
    def test_status(self, postgres_conn_dto: MySqlInfoIDto) -> bool:
        try:
            psycopg2.connect(
                host=postgres_conn_dto.host,
                port=postgres_conn_dto.port,
                database=postgres_conn_dto.database,
                user=postgres_conn_dto.user,
                password=postgres_conn_dto.password,
            )
            return True
        except OperationalError as _:
            return False


postgresql_driver_impl = PostgreSqlDriver()
