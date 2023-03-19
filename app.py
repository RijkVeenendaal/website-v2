from flask import Flask, render_template, jsonify

href="{{ url_for('static', filename='images/plaatje.png', filename='images/office.webp') }}"

JOBS = [
  {
    'id' : 1,
    'title' : 'Data Analist',
    'location' : 'Arnhem, Netherlands',
    'salary' : '€ 3.500,00'  
  },
   {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Arnhem, Netherlands',
    'salary' : '€ 6.000,00'
  },
     {
    'id' : 3,
    'title' : 'Frontend Engineer',
    'location' : 'Arnhem, Netherlands',
    'salary' : '€ 5.000,00'
  },
     {
    'id' : 4,
    'title' : 'Backend Engineer',
    'location' : 'Arnhem, Netherlands',
    'salary' : '€ 5.000,00'
  },
]


app = Flask(__name__)

@app.route("/")
def Hello_World():
  return render_template('index.html', jobs=JOBS, company='Rijk')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
