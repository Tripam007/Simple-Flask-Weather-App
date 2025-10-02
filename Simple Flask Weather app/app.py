from flask import Flask, render_template, request
import requests

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None

    if request.method == "POST":
        city = request.form.get("city") 
        if city:
            url = f"https://api.weatherapi.com/v1/current.json?key=b17a4020b41e41eba8472905250108&q={city}" #weather api key 
            res = requests.get(url).json()

            if "error" not in res:
                weather_data = {
                    "city": res["location"]["name"],
                    "region": res["location"]["region"],
                    "country": res["location"]["country"],
                    "temperature": res["current"]["temp_c"],
                    "feelslike": res["current"]["feelslike_c"],
                    "condition": res["current"]["condition"]["text"],
                    "humidity": res["current"]["humidity"],
                    
                }
            else:
                weather_data = {"error": "City not found 😕"} #if city name not found display this message

    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
