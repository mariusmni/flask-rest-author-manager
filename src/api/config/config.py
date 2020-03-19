class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'top secret key'
    SECRET_KEY= 'your_secured_key_here'
    SECURITY_PASSWORD_SALT= 'your_security_password_here'
    
    MAIL_DEFAULT_SENDER= 'user@yahoo.com'
    MAIL_SERVER= 'smtp.mail.yahoo.com'
    MAIL_PORT= 465
    MAIL_USERNAME= 'user'
    MAIL_PASSWORD= 'mypass?'
    MAIL_USE_TLS= False
    MAIL_USE_SSL= True

    UPLOAD_FOLDER = 'images'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marius:password@localhost:3306/proddb'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://marius:password@localhost:3306/devdb'
    SQLALCHEMY_ECHO = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    JWT_SECRET_KEY = 'JWT-SECRET'
    SECRET_KEY = 'SECRET-KEY'
    SECURITY_PASSWORD_SALT = 'PASSWORD-SALT'
    MAIL_DEFAULT_SENDER = ''
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    UPLOAD_FOLDER = 'images'

