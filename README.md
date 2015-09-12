# djangoslackbridge
Django based app for linking two Slack channels together

1. clone the repo
2. create virtualenv 
3. activate virtualenv
4. ```pip install -r requirements.txt```
5. ```python manage.py makemigrations```
6. ```python manage.py migrate``` # you'll be prompted for a new superuser
7. ```python manage.py runserver```
8. goto the url for your app, add ```/admin```, login
9. add a bridge 

Enjoy !

Some Slack related notes:

1. You need on outgoing webhook from the source channel, pointing to ```http://yoursite.com/bridge/``` # the trailing slash is needed
2. you need at least one incoming web hook as a destination for your bridge, and the destination channel-name

