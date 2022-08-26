import pickle 
import json
import config
import numpy as np

class AutoDetaset():
    def __init__(self,symboling,normalized_losses,fuel_type,aspiration,num_of_doors,
                    drive_wheels,engine_location,wheel_base,length,width,
                    height,curb_weight,num_of_cylinders,engine_size,bore,stroke,
                    compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg,
                    body_style,engine_type,fuel_system):
        
        self.symboling = symboling
        self.normalized_losses = normalized_losses
        self.fuel_type = fuel_type
        self.aspiration = aspiration
        self.num_of_doors = num_of_doors
        self.drive_wheels = drive_wheels
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width
        self.height = height
        self.curb_weight = curb_weight
        self.num_of_cylinders = num_of_cylinders
        self.engine_size = engine_size
        self.bore = bore
        self.stroke = stroke
        self.compression_ratio = compression_ratio
        self.horsepower = horsepower
        self.peak_rpm = peak_rpm
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.engine_location = engine_location
        self.wheel_base = wheel_base
        self.length = length
        self.width = width

        self.body_style = "body-style_" + body_style
        self.engine_type = "engine-type_" + engine_type
        self.fuel_system = "fuel-system_" + fuel_system

        
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)

    def get_p_price(self):
        self.load_model()
        body_style_index = self.json_data['Columns'].index(self.body_style)
        engine_type_index = self.json_data['Columns'].index(self.engine_type)
        fuel_system_index = self.json_data['Columns'].index(self.fuel_system)

        test_array = np.zeros(len(self.json_data['Columns']))
        
        test_array[0] = self.symboling
        test_array[1] = self.normalized_losses
        test_array[2] = self.json_data['fuel_type_values'][self.fuel_type] #
        test_array[3] = self.aspiration
        test_array[4] = self.json_data['Num_of_Doors'][self.num_of_doors] #
        test_array[5] =self.drive_wheels 
        test_array[6] =self.engine_location 
        test_array[7] =self.wheel_base
        test_array[8] =self.length 
        test_array[9] =self.width 
        test_array[10] =self.height 
        test_array[11] =self.curb_weight 
        test_array[12] =self.json_data['num_of_cylinders_values'][self.num_of_cylinders] #
        test_array[13] =self.engine_size 
        test_array[14] =self.bore 
        test_array[15] =self.stroke
        test_array[16] =self.compression_ratio 
        test_array[17] =self.horsepower
        test_array[18] =self.peak_rpm 
        test_array[19] =self.city_mpg
        test_array[20] =self.highway_mpg 

        test_array[body_style_index] = 1
        test_array[engine_type_index] = 1
        test_array[fuel_system_index] = 1

        print("Test Array :",test_array)

        predicted_price = np.around(self.model.predict([test_array])[0],2)
        return predicted_price

