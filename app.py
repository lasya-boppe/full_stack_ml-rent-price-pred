import csv
from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

def load_data():
    with open('FINAL.csv', mode = 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

houses = load_data()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/houses', methods = ['GET'])
def get_houses():
    return jsonify({'count':len(houses),
                    'houses': houses})

@app.route('/view-spec')
def view_spec():
    return render_template('view_specifications.html')

@app.route('/view-spec/bystatus')
def view_spec_bystatus():
    return render_template('bystatus.html') 


@app.route('/view-spec/bystatus/display', methods = ['GET'])
def view_by_status():
    stat = request.args.get('status')
    filtered = [h for h in houses if h.get('Status') == stat]
    filtered_dict ={'count': len(filtered),
                    'houses':filtered}
    return jsonify(filtered_dict)

@app.route('/view-spec/bybedrooms')
def view_spec_by_bedrooms():
    return render_template('bybedrooms.html')

@app.route('/view-spec/bybedrooms/display', methods = ['GET'])
def view_by_bedrooms():
    beds = request.args.get('beds')
    if not beds:
        return jsonify({'error':'Invalid input for number of bedrooms'})
    try:
        beds_float = float(beds)
    except ValueError:
        return jsonify({'error':'Invalid input for number of bedrooms'})
    filtered = [h for h in houses if h.get('BHK') and float(h.get('BHK','')) == beds_float]
    filtered_dict = {'count' : len(filtered),
                     'houses': filtered}
    return jsonify(filtered_dict)

@app.route('/view-spec/bytype')
def view_spec_by_type():
    return render_template('bytype.html')

@app.route('/view-spec/bytype/display', methods = ['GET'])
def view_by_type():
    types = request.args.get('types')
    if not types:
        return jsonify({'Error':'Invalid input for type of house'})
    try:
        types = types
    except ValueError:
        return jsonify({'Error':'Invalid input for type of house'})
    filtered =[h for h in houses if h.get('Type') and h.get('Type') == types]
    filtered_dict = {'count':len(filtered),
                     'houses':filtered}
    return jsonify(filtered_dict)


@app.route('/api/houses/add', methods = ['GET'])
def add_house_interface():
    return render_template('add_house.html')

@app.route('/api/houses/adding', methods=['POST'])
def add_house():
    new_house = {
        'No': len(houses)+1,
        'BHK': request.form.get('bedrooms'),
        'Location': request.form.get('address'),
        'Price': request.form.get('price'),
        'Sqft': request.form.get('sqft'),
        'Status': request.form.get('status'),
        'Deposit': request.form.get('deposit'),
        'Availability': request.form.get('avail'),
        'Bathrooms': request.form.get('baths'),
        'Facing': request.form.get('facing')
    }

    houses.append(new_house)
    return jsonify({'message' : 'House added successfully',
                    'Count' : len(houses)})

if __name__ == '__main__':
    app.run(debug=True)