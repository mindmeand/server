from datetime import datetime
from config import Config
from flask import request
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, jwt_required
from flask_restful import Resource
from mysql_connection import get_connection
from mysql.connector import Error
from email_validator import validate_email, EmailNotValidError
from utils import check_password, hash_password
import openai

# chat-gpt
class ConsultationResource(Resource) :
    # 고민 상담 API ( 질문과 응답을 DB에 저장 )
    @jwt_required()
    def post(self) :
    
        # 상담 기능 

        userId = get_jwt_identity()
        data = request.get_json()
        content = data["question"]
        
        openai.api_key = Config.openAIKey

        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a caring and empathetic trouble counselor who listens to people's concerns and provides warm and supportive advice."},
                {"role": "user", "content": content}
            ]
        )

        print(completion.choices[0].message['content'].strip())

        response_message = completion.choices[0].message['content'].strip()

        # DB에 저장
        try : 
            connection = get_connection()
            query = '''insert into consultation
                    (userId,question,response)
                    values
                    (%s,%s,%s)'''
            record = (userId,content,response_message)
            cursor = connection.cursor()
            cursor.execute(query,record)
            connection.commit()
            cursor.close()
            connection.close()

        except Error as e :
            print(e)
            cursor.close()
            connection.close()
            return{'error':str(e)},500
        
        return {'result':'success'},200

