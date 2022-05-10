def recommended_crops(results):
    categories = ['apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee',
       'cotton', 'grapes', 'jute', 'kalabasa', 'kamatis', 'kidneybeans',
       'lentil', 'maize', 'mango', 'mothbeans', 'mungbean', 'muskmelon',
       'okra', 'orange', 'papaya', 'pigeonpeas', 'pomegranate', 'rice',
       'sili', 'sitaw', 'talbos ng kamote', 'talong', 'watermelon']

    probability_crops = dict(zip(categories, [x for x in results[0]]))

    crop_list = sorted(probability_crops.items(), key=lambda x:x[1])

    recommended = ""
    for a in range(len(categories)):
        crop = crop_list[(-a-1)]
        recommended += crop[0]
        if a == 2:
            break
        recommended += ","

    return recommended