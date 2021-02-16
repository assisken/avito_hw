FROM postgres:latest

ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=metrics_db

EXPOSE 5432

COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
