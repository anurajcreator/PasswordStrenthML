from flask_restx import Resource
from app.main.service.password_prediction_service import password_strength_predict
from app.main.util.password_classification_dto import PasswordClassificationDto
from flask import request

api = PasswordClassificationDto.api 
_password_pred = PasswordClassificationDto.password_pred

@api.route('/predict')
class PasswordPrediction(Resource):
    @api.doc('Password Strenth Prediction')
    @api.expect(_password_pred) 
    def post(self):
        """Password Strenth Prediction"""
        return password_strength_predict(request)