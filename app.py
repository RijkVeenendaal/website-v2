from flask import Flask, render_template

href="{{ url_for('static', filename='images/plaatje.png') }}"

app = Flask(__name__)

@app.route("/")
def Hello_World():
  return render_template('index.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
