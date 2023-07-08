from flask import Flask
from config import Config

app=Flask(__name__,template_folder='templates',static_folder='static')
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()

import routes