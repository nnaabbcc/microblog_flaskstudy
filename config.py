
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# Remove warning 'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be 
# disabled by default in the future.  Set it to True to suppress this 
# warning.'
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = '48b0ed7b-f1cb-47cd-be30-b8a560421c6f'

OPENID_PROVIDERS = [
        { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
        { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
        { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
        { 'name': 'Flickr', 'url': 'https://www.flickr.com/<username>' },
        { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
