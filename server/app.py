# #!/usr/bin/env python3
# from models import db, Restaurant, RestaurantPizza, Pizza
# from flask_migrate import Migrate
# from flask import Flask, request, make_response
# from flask_restful import Api, Resource
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# api = Api(app)


# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"


# if __name__ == "__main__":
#     app.run(port=5555, debug=True)


# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from models import db, Restaurant, RestaurantPizza, Pizza

# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db.init_app(app)
# migrate = Migrate(app, db)


# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"


# @app.route("/restaurants")
# def get_restaurants():
#     restaurants = Restaurant.query.all()
#     return jsonify([restaurant.to_dict() for restaurant in restaurants])


# @app.route("/restaurants/<int:id>")
# def get_restaurant(id):
#     restaurant = Restaurant.query.get_or_404(id)
#     return jsonify(restaurant.to_dict())


# @app.route("/pizzas")
# def get_pizzas():
#     pizzas = Pizza.query.all()
#     return jsonify([pizza.to_dict() for pizza in pizzas])


# @app.route("/restaurant_pizzas", methods=["POST"])
# def create_restaurant_pizza():
#     data = request.json
#     restaurant_id = data.get("restaurant_id")
#     pizza_id = data.get("pizza_id")
#     price = data.get("price")

#     if not all([restaurant_id, pizza_id, price]):
#         return jsonify({"error": "Missing required parameters"}), 400

#     restaurant = Restaurant.query.get(restaurant_id)
#     pizza = Pizza.query.get(pizza_id)

#     if not restaurant or not pizza:
#         return jsonify({"error": "Restaurant or Pizza not found"}), 404

#     restaurant_pizza = RestaurantPizza(
#         restaurant_id=restaurant_id, pizza_id=pizza_id, price=price
#     )
#     db.session.add(restaurant_pizza)
#     db.session.commit()

#     return jsonify(restaurant_pizza.to_dict()), 201


# @app.route("/restaurants/<int:id>", methods=["DELETE"])
# def delete_restaurant(id):
#     restaurant = Restaurant.query.get_or_404(id)
#     db.session.delete(restaurant)
#     db.session.commit()
#     return "", 204


# if __name__ == "__main__":
#     app.run(port=5555, debug=True)


# #!/usr/bin/env python3
# from models import db, Restaurant, RestaurantPizza, Pizza
# from flask_migrate import Migrate
# from flask import Flask, request, make_response
# from flask_restful import Api, Resource
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# api = Api(app)


# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"


# class Restaurants(Resource):
#     def get(self):
#         restaurants = [
#             r.to_dict(rules=["-restaurant_pizzas"]) for r in Restaurant.query.all()
#         ]
#         return make_response(restaurants, 200)


# api.add_resource(Restaurants, "/restaurants")


# class RestaurantByID(Resource):
#     def get(self, id):
#         try:
#             restaurant = Restaurant.query.filter_by(id=id).first().to_dict()

#             return make_response(restaurant, 200)
#         except Exception as error:
#             print(error)
#             return make_response({"error": "Restaurant not found"}, 404)

#     def delete(self, id):
#         restaurant = Restaurant.query.get(id)
#         if restaurant:
#             db.session.delete(restaurant)
#             db.session.commit()
#             return make_response("", 204)
#         else:
#             return make_response({"error": "Restaurant not found"}, 404)

# api.add_resource(RestaurantByID, "/restaurants/<int:id>")

# #     def delete(self, id):
# #         try:
# #             restaurant = Restaurant.query.filter_by(id=id).first()

# #             if restaurant:
# #                 db.session.delete(restaurant)
# #                 db.session.commit()

# #             restaurant_after_deletion = Restaurant.query.filter_by(id=id).first()

# #             if restaurant_after_deletion == None:
# #                 return make_response({"message": "deletion is successful"}, 204)
# #         except Exception as error:
# #             print(error)
# #             return make_response({"error": "deletion is unsuccessful"}, 500)


# # api.add_resource(RestaurantByID, "/restaurants/<int:id>")


# class Pizzas(Resource):
#     def get(self):
#         pizzas = [p.to_dict(rules=["-restaurant_pizzas"]) for p in Pizza.query.all()]
#         return make_response(pizzas, 200)


# api.add_resource(Pizzas, "/pizzas")


# class RestaurantPizzas(Resource):
#     def post(self):
#         try:
#             data = request.get_json()

#             new_rp = RestaurantPizza(
#                 price=data["price"],
#                 pizza_id=data["pizza_id"],
#                 restaurant_id=data["restaurant_id"],
#             )

#             db.session.add(new_rp)
#             db.session.commit()

#             return make_response(new_rp.to_dict(), 201)
#         except Exception as error:
#             print(error)

#             return make_response({"errors": ["validation errors"]}, 400)


# api.add_resource(RestaurantPizzas, "/restaurant_pizzas")

# if __name__ == "__main__":
#     app.run(port=5555, debug=True)


# #!/usr/bin/env python3
# from models import db, Restaurant, RestaurantPizza, Pizza
# from flask_migrate import Migrate
# from flask import Flask, request, make_response
# from flask_restful import Api, Resource
# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.json.compact = False

# migrate = Migrate(app, db)

# db.init_app(app)

# api = Api(app)

# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"

# class Restaurants(Resource):

#     def get(self):
#         restaurants = [
#             restaurant.to_dict(only=("id", "address", "name"))
#             for restaurant in Restaurant.query.all()
#         ]
#         return make_response(restaurants, 200)


# api.add_resource(Restaurants, "/restaurants")


# class RestaurantsByID(Resource):

#     def get(self, id):
#         restaurant = Restaurant.query.filter_by(id=id).first()

#         if restaurant:
#             response = restaurant.to_dict(
#                 rules=(
#                     "-restaurantpizzas.restaurant",
#                     "-restaurantpizzas.pizza.restaurantpizzas",
#                 )
#             )
#             response["restaurant_pizzas"] = response.pop("restaurantpizzas")
#             return make_response(response, 200)
#         else:
#             response = make_response({"error": "Restaurant not found"}, 404)
#             return response

#     def delete(self, id):
#         restaurant = db.session.get(Restaurant, id)

#         if restaurant:
#             db.session.delete(restaurant)
#             db.session.commit()
#             response = {}
#             return make_response(response, 204)
#         else:
#             response = {"error": "Restaurant not found"}
#             return make_response(response, 404)


# api.add_resource(RestaurantsByID, "/restaurants/<int:id>")


# class Pizzas(Resource):
#     def get(self):
#         pizzas = [
#             pizza.to_dict(only=("id", "ingredients", "name"))
#             for pizza in Pizza.query.all()
#         ]
#         return make_response(pizzas, 200)


# api.add_resource(Pizzas, "/pizzas")


# class RestaurantPizzas(Resource):

#     def post(self):
#         try:
#             new_restaurant_pizza = RestaurantPizza(
#                 price=request.json.get("price"),
#                 pizza_id=request.json.get("pizza_id"),
#                 restaurant_id=request.json.get("restaurant_id"),
#             )
#             db.session.add(new_restaurant_pizza)
#             db.session.commit()
#             response = new_restaurant_pizza.to_dict(
#                 rules=("-restaurant.restaurantpizzas", "-pizza.restaurantpizzas")
#             )
#             return make_response(response, 201)
#         except:
#             response_body = {"errors": ["validation errors"]}
#             return make_response(response_body, 400)


# api.add_resource(RestaurantPizzas, "/restaurant_pizzas")


# if __name__ == "__main__":
#     app.run(port=5555, debug=True)


from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask, request, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)


@app.route("/")
def index():
    return "<h1>Code challenge</h1>"


class Restaurants(Resource):
    def get(self):
        restaurants = [
            restaurant.to_dict(only=("id", "address", "name"))
            for restaurant in Restaurant.query.all()
        ]
        return make_response(restaurants, 200)


api.add_resource(Restaurants, "/restaurants")


class RestaurantsByID(Resource):
    def get(self, id):
        try:
            restaurant = Restaurant.query.filter_by(id=id).first_or_404()
            response = restaurant.to_dict(
                rules=(
                    "-restaurant_pizzas.restaurant",
                    "-restaurant_pizzas.pizza.restaurant_pizzas",
                )
            )
            response["restaurant_pizzas"] = response.pop("restaurant_pizzas")
            return make_response(response, 200)
        except Exception as e:
            print(e)
            return make_response({"error": "Restaurant not found"}, 404)

    def delete(self, id):
        try:
            restaurant = db.session.get(Restaurant, id)
            if restaurant:
                db.session.delete(restaurant)
                db.session.commit()
                return make_response("", 204)
            else:
                return make_response({"error": "Restaurant not found"}, 404)
        except Exception as e:
            print(e)
            return make_response({"error": "An error occurred"}, 500)


api.add_resource(RestaurantsByID, "/restaurants/<int:id>")

 
class Pizzas(Resource):
    def get(self):
        pizzas = [
            pizza.to_dict(only=("id", "ingredients", "name"))
            for pizza in Pizza.query.all()
        ]
        return make_response(pizzas, 200)


api.add_resource(Pizzas, "/pizzas")


class RestaurantPizzas(Resource):
    def post(self):
        try:
            data = request.get_json()
            new_restaurant_pizza = RestaurantPizza(
                price=data["price"],
                pizza_id=data["pizza_id"],
                restaurant_id=data["restaurant_id"],
            )
            db.session.add(new_restaurant_pizza)
            db.session.commit()
            response = new_restaurant_pizza.to_dict(
                rules=("-restaurant.restaurant_pizzas", "-pizza.restaurant_pizzas")
            )
            return make_response(response, 201)
        except Exception as e:
            print(e)
            return make_response({"errors": ["validation errors"]}, 400)


api.add_resource(RestaurantPizzas, "/restaurant_pizzas")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
