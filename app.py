from flask import Flask
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from resources.user import User, UserRegister, UserLogin
from con_sql_alchemy import bd
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hoteis.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "a_minha_chave_secreta_longa_e_intransmissivel"

api.add_resource(Hoteis,"/hoteis")
api.add_resource(Hotel,"/hoteis/<string:hotel_id>")
api.add_resource(User,"/users/<string:username>")
api.add_resource(UserRegister,"/registar")
api.add_resource(UserLogin, "/login")

if __name__ == "__main__":
    bd.init_app(app)
    with app.app_context():
        bd.create_all()
    app.run(debug=True) 
    