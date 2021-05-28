from flask import Flask , redirect , url_for ,render_template , request, jsonify
import pgeocode
from utils import *
from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = 'geoapiExercise')
data = pgeocode.Nominatim('In')

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def home():
    return render_template('datainput.html')

@app.route("/" , methods=['POST','GET'])
def address():
    if request.method == "POST":
        pincode = request.form["pincode"]
        return redirect(url_for("pincode",pin=pincode))
    else:
        return render_template('datainput.html')

@app.route("/axis" , methods=['POST','GET'])
def axis():
    if request.method == "POST":
        latitude = request.form["latitude"]
        longitude = request.form["longitude"]

        return redirect(url_for("getAddressByAxis",latitude=latitude,longitude=longitude))
    else:
        return render_template('datainput.html')

@app.route("/<latitude>/<longitude>")
def getAddressByAxis(latitude,longitude):
    location = geocoder.reverse((latitude, longitude))
    return jsonify(detailedAddress(location.raw['address']))

@app.route("/<pin>")
def pincode(pin):
    location=(data.query_postal_code(str(pin)))
   
    return jsonify(detailedAddress(location))


app.run()
