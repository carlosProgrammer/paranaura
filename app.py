import json
from collections import OrderedDict
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)
# Used to modify the attribute to return desired interface.
app.config['JSON_SORT_KEYS'] = False


# Error handling on 400 Bad Request & 404 Not found
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': '400 Bad Request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': '404 Not Found'}), 404)


# Loading and manipulating files using 'with' parameter.
with open('companies.json', 'r') as file:
    companies_list = json.load(file)

companies_by_id = {}
companies_by_name = {}
for company in companies_list:
    companies_by_id[company['index']] = company['company']
    companies_by_name[company['company']] = company['index']

with open('people.json', 'r') as file:
    people_list = json.load(file)


# API routes and functions
@app.route('/paranaura/api/v1.0/company/<string:company_name>', methods=['GET'])
# Function to get all its employees if it's the case.
def get_employees(company_name):
    if company_name.upper() not in companies_by_name:
        abort(400)
    company_id = companies_by_name[company_name.upper()]
    employees = []
    for person in people_list:
        if person['company_id'] == company_id:
            employees.append({'index': person['index'], 'name': person['name']})
    return jsonify(employees)


@app.route('/paranaura/api/v1.0/people/<int:id1>/<int:id2>', methods=['GET'])
# Function to get people's information (name, age, address, phone) and if they have friends in common alive &
# with brown eyes they will be returned.
def get_friends(id1, id2):
    lim = len(people_list)
    if id1 not in range(lim) or id2 not in range(lim):
        abort(400) # Bad request to prevent misleading 404 results.
    p_1 = people_list[id1]
    p_2 = people_list[id2]
    keys = ['name', 'age', 'address', 'phone']
    person_1 = {key: p_1[key] for key in keys}
    person_2 = {key: p_2[key] for key in keys}
    friends_1 = [friend['index'] for friend in p_1['friends']]
    friends_2 = [friend['index'] for friend in p_2['friends']]
    common_friends = list(set(friends_1).intersection(friends_2))
    common_friends_selected = []
    for i in common_friends:
        friend = people_list[i]
        if friend['eyeColor'] == 'brown' and not friend['has_died']:
            common_friends_selected.append(i)
    return jsonify({'person_1': person_1,
                    'person_2': person_2,
                    'common_friends': common_friends_selected})


# Available fruits and vegetables
fruits = {'banana', 'cucumber', 'strawberry', 'apple', 'orange'}
vegetables = {'celery', 'beetroot', 'carrot'}


@app.route('/paranaura/api/v1.0/people/<int:person_id>', methods=['GET'])
# Function to list a person's favourite fruits and vegetables.
def get_food(person_id):
    person = people_list[person_id]
    user = dict()
    user['username'] = person['name']
    user['age'] = person['age']
    user['fruits'] = [item for item in person['favouriteFood'] if item in fruits]
    user['vegetables'] = [item for item in person['favouriteFood'] if item in vegetables]
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=False)
