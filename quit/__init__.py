import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # from . import game
    # app.register_blueprint(game.bp)

    # app.add_url_rule('/', endpoint='index')

    @app.route('/')
    def base():
        return render_template('base.html')

    return app
