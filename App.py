from flask_migrate import Migrate
from routes.panel.UserRoute import UserRoute
from config import db, app

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)


## bot
## panel admin
app.register_blueprint(UserRoute, url_prefix='/users')

if __name__ == '__main__':
    app.debug = True
    app.run()