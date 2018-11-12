from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, generate_csrf
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
# 创建SQLALCHEMY对象
db = SQLAlchemy(app)

# 开启csrf保护
CSRFProtect(app)

# 注册路由
from app.index import index_blue
app.register_blueprint(index_blue)


