from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SUBSTITUTIONS = {
    'milk': ['almond milk', 'soy milk', 'oat milk'],
    'egg' : ['applesauce', 'banana', 'chia seeds'],
    'peanut': ['almond', 'sunflower seeds', 'pumpkin seeds'],
}

@app.route('/suggest_substitutes', methods=['POST'])

def suggest_substitutes():
    data = request.json
    ingredients = [ingredient.lower() for ingredient in data.get('ingredients',[])]
    user_allergens = [allergen.lower() for allergen in data.get('allergens', [])]
    substitutes = {}

    for ingredient in ingredients:
        if ingredient in user_allergens:
           if ingredient in SUBSTITUTIONS:
               
               valid_substitutes = [
                   substitute for substitute in SUBSTITUTIONS[ingredient]
                   if substitute.lower() not in user_allergens
               ]

               if valid_substitutes:
                   substitutes[ingredient] = valid_substitutes

    
    return jsonify({'substitutes': substitutes})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)