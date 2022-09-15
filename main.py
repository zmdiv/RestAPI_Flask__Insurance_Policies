from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import json

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        data = pd.read_csv('policies.csv')
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code

    def post(selfs):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', required=True, type=str)
        parser.add_argument('policy_num', required=True, type=str)
        parser.add_argument('name', required=True, type=str)
        parser.add_argument('surname', required=True, type=str)
        parser.add_argument('dob', required=True, type=str)
        parser.add_argument('sex', required=True, type=str)
        parser.add_argument('country', required=True, type=str)
        parser.add_argument('start_date', required=True, type=str)
        parser.add_argument('finish_date', required=True, type=str)
        parser.add_argument('travel_area', required=True, type=str)
        args = parser.parse_args()

        data = pd.read_csv('policies.csv')

        if args['user_id'] in data['user_id']:
            return {'message': 'user already exists', 409}
        else:
            data = data.append({
                'user_id': args['user_id'],'policy_num': args['policy_num']
                'name': args['name'], 'surname': args['surname'], 'dob': args['dob'],
                'sex': args['sex'], 'country': args['country'], 'start_date': args['start_date'],
                'finish_date': args['finish_date'], 'travel_area': args['travel_area']},
                ignore_index=True
            )
            return {'data' : data.to_dict()}, 200

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument()


class Locations(Resource):
    # methods go here
    pass


api.add_resource(Users, '/users')  # '/users' is our entry point for Users
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations

if __name__ == '__main__':
    app.run()
