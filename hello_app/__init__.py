from flask import Flask  # Import the Flask class
import os, logging
from . import config as dev_config
from flask_session import Session

def create_app():
    app = Flask(__name__)    # Create an instance of the class for our use
    app.logger.info(f"Environment set in app.config is {app.config.get('ENV')}")
    if app.config.get('ENV') == 'production':
        app.logger.level=logging.INFO
        app.logger.error("ARE YOU SURE?")
        # if you are certain you want to run in prod,
        # supply a production config and remove this line:
        raise ValueError('This app is not meant to run in production. Run it according to instructions at top of this file.')
    elif app.config.get('ENV') == 'development':
        app.logger.level=logging.DEBUG
        # app.config.from_object(dev_config)
    else:
        raise ValueError('production and development are the only options')
    #
    # if config_dict is not None:
    #         app.config.from_mapping(config_dict)

    # init the serverside session on the app
    Session(app)

    # We have to push the context before registering auth endpoints blueprint
    app.app_context().push()
    # from . import auth_endpoints
    #
    # # register the auth endpoints! These are:
    # # sign-in status
    # # token details
    # # redirect
    # # sign in
    # # sign out
    # # post sign-out
    # app.register_blueprint(auth_endpoints.auth)
    return app

app=create_app()