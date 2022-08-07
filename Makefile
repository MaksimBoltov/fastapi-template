revision:
	alembic revision --autogenerate

upgrade:
	alembic upgrade head

runserver:
	uvicorn app.main:app --reload