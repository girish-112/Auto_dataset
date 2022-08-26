import re
from flask import Flask,jsonify,request
from project_app.utils import AutoDetaset
import config

app = Flask(__name__)

@app.route('/')
def home_api():
    return "We Are in First API"

@app.route('/predict_charges')
def get_price():
    data = request.form

    symboling = eval(data['symboling'])
    normalized_losses = eval(data['normalized_losses'])
    fuel_type = data['fuel_type']
    aspiration = eval(data['aspiration'])
    num_of_doors = data['num_of_doors']
    drive_wheels = eval(data['drive_wheels'])
    engine_location = eval(data['engine_location'])
    wheel_base = eval(data['wheel_base'])
    length = eval(data['length'])
    width = eval(data['width'])
    height = eval(data['height'])
    curb_weight = eval(data['curb_weight'])
    num_of_cylinders = data['num_of_cylinders']
    engine_size = eval(data['engine_size'])
    bore = eval(data['bore'])
    stroke = eval(data['stroke'])
    compression_ratio = eval(data['compression_ratio'])
    horsepower = eval(data['horsepower'])
    peak_rpm = eval(data['peak_rpm'])
    city_mpg = eval(data['city_mpg'])
    highway_mpg = eval(data['highway_mpg'])
    body_style = data['body_style']
    engine_type = data['engine_type']
    fuel_system = data['fuel_system']


    f_price = AutoDetaset(symboling,normalized_losses,fuel_type,aspiration,num_of_doors,
                    drive_wheels,engine_location,wheel_base,length,width,
                    height,curb_weight,num_of_cylinders,engine_size,bore,stroke,
                    compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,
                    body_style,engine_type,fuel_system)

    charges = f_price.get_p_price()
    return jsonify({"Predicted Price = " : f"{charges}"})

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port = config.PORT_NUMBER,debug=False)
    
        