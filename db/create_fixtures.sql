CREATE TABLE IF NOT EXISTS metrics (
	ID SERIAL PRIMARY KEY NOT NULL,
	DATE_M DATE NOT NULL,
	VIEWS INT,
	CLICKS INT,
	COST MONEY
);