from flask import Flask, jsonify, request
from keras.models import load_model
from probability import recommended_crops
import pandas as pd
import warnings

app = Flask(__name__)


@app.route('/crop_recommendation', methods=['POST'])
def crop_recommendation():
    nitrogen_content = request.json.get('n')
    phosphorous_content = request.json.get('p')
    potassium_content = request.json.get('k')
    temperature = request.json.get('temp')
    humidity = request.json.get('hum')
    ph_level_content = request.json.get('ph')
    rainfall = request.json.get('rain')

    input_df = pd.DataFrame({'N': [nitrogen_content],
                         'P': [phosphorous_content],
                         'K': [potassium_content],
                         'temperature': [temperature],
                         'humidity': [humidity],
                         'ph': [ph_level_content],
                         'rainfall': [rainfall]})

    crop_model = load_model('lstm_model.h5')
    result = crop_model.predict(input_df)
    crops = recommended_crops(result)

    crop_json = {
                    "crops": crops
                }

    return jsonify(crop_json)

if __name__ == "__main__":
    warnings.simplefilter('ignore')
    app.run()