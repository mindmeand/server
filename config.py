
class Config :
    HOST = ''
    DATABASE = ''
    DB_USER = ''
    DB_PASSWORD = ''

    SALT = 'dskj29jcdn12jn'

    # JWT 관련 변수를 셋팅
    JWT_SECRET_KEY = 'yhacdemy20230105##hello'
    JWT_ACCESS_TOKEN_EXPIRES = False # 만료없이 설정
    PROPAGATE_EXCEPTIONS = True # 에러가 나면 보여줄것