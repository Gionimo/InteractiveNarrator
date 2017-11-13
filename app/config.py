import os
import launch
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

ALLOWED_EXTENSIONS = set(['txt', 'csv'])
UPLOAD_FOLDER = 'uploads/'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# set the secret key.  keep this really secret:
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['interactivenarratoruu@gmail.com']