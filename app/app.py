from flask import Flask, request, jsonify
import psycopg2

con = psycopg2.connect(
  database='metrics_db',
  user='admin',
  host='db',
  password='admin',
  port='5432'
)
# Init app
app = Flask(__name__)

# Create a metrics
@app.route('/metrics', methods=['POST'])
def add_metrics():
  print("Eto POST, suchka!")
  date = request.json['date']
  views = request.json['views']
  clicks = request.json['clicks']
  cost = request.json['cost']
  cur=con.cursor()
  cur.execute('''INSERT INTO metrics (DATE_M,VIEWS,CLICKS,COST)
  				VALUES (%(date)s, %(views)s, %(views)s, %(cost)s)''',
                {'date': date, 'views': views, 'clicks': clicks, 'cost': cost})
  con.commit()
  print("Work!")
  return "OK"
# Get Single metricss
@app.route('/metrics/<date>&<date1>', methods=['GET'])
def get_metrics(date,date1):
  cur=con.cursor()
  cur.execute('''SELECT date_m, SUM(views), SUM(clicks), SUM(cost) FROM metrics
  				WHERE date_m BETWEEN %(date)s AND %(date1)s
  				GROUP BY date_m
  				ORDER BY date_m''',
                {'date': date, 'date1': date1})
  print("Work!Get")
  print(cur.fetchall())
  return "OK"

# Delete metrics
@app.route('/metrics', methods=['DELETE'])
def delete_metrics():
  print("Delete, suchka")
  cur=con.cursor()
  cur.execute("DELETE FROM metrics")
  con.commit()
  return "Database cleared!"

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
