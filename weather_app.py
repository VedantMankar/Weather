from flask import Flask,render_template,request
import requests


app = Flask(__name__)

@app.route("/temperature",methods=['POST'])
def temperature():
    city_name = request.form['name']

    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_name+",IN&appid=1451dfb941b8c1d8330a5179f96ef749")
    json_data = r.json()
    temp_k = float(json_data['main']['temp'])
    temp_f = (temp_k-273.15)*1.8 + 32
    return render_template("weather.html",temp=temp_f)


#url = "http://api.openweathermap.org/data/2.5/weather?appid=1451dfb941b8c1d8330a5179f96ef749&q={}"

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)