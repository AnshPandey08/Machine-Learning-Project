import json
import pickle
import os
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
        
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0])
def get_location_names():
    return __locations

def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations
    global __model

    # Use the directory of the current file as the base path
    base_path = os.path.dirname(__file__)
    columns_path = os.path.join(base_path, "artifacts", "columns.json")
    model_path = os.path.join(base_path, "artifacts", "banglore_home_prices_model.pickle")

    
    # Load columns.json
    try:
        with open(columns_path, 'r') as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]
    except FileNotFoundError:
        print(f"Error: {columns_path} not found.")
        return

    global __model
    # Load model pickle file
    try:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)
    except FileNotFoundError:
        print(f"Error: {model_path} not found.")
        return

    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,2))
    print(get_estimated_price('Kalhali',1000,2,2))  #other location
    print(get_estimated_price('Ejipura',1000,2,2))  #other location
    
    