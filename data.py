import generators

class WrongDataForLoginUser:
    wrong_data_for_login_user = {"email": "wrong_email@yandex.ru", "password": "wrong_password"}


class MissingDataForUser:
    user_creation_with_missing_field = [
        {'email': generators.email_generator(),
         'password': generators.password_generator(),
         'name': ''},
        {'email': generators.email_generator(),
         'password': '',
         'name': generators.name_generator()},
        {'email': '',
         'password': generators.password_generator(),
         'name': generators.name_generator()}
    ]

class Url:
    MAIN_URL = ' https://stellarburgers.nomoreparties.site'
    CREATE_USER = f'{MAIN_URL}/api/auth/register' # POST
    LOGIN_USER = f'{MAIN_URL}/api/auth/login'  # POST
    LOGOUT_USER = f'{MAIN_URL}/api/auth/logout'  # POST
    REFRESH_TOKEN = f'{MAIN_URL}/api/auth/token'  # POST
    DELETE_USER = f'{MAIN_URL}/api/auth/user'  # DELETE
    CREATE_ORDER = f'{MAIN_URL}/api/orders'  # POST
    GET_INGREDIENTS = f'{MAIN_URL}/api/ingredients' #GET

class ResponseBody:
    USER_EXIST = {"success": False, "message": "User already exists"} #403 Forbidden
    USER_FIELD_MISSING = {"success": False, "message": "Email, password and name are required fields"} #403 Forbidden
    USER_UNAUTHORIZED = {"success": False, "message": "email or password are incorrect"} #401 Unauthorized
    USER_REFRESH_UNAUTHORIZED = {"success": False,"message": "You should be authorised"} #401 Unauthorized
    INGREDIENTS_NOT_TRANSFER = {"success": False,"message": "Ingredient ids must be provided"} #400 Bad Request

class OrderIngredients:
    create_order_variants = [
        (['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa72'], 200),  # с ингредиентами
        ([], 400),  # без ингредиентов
        (['61c0c5a71d1f82001bdbbb6f'], 500)  # c неверным хешем ингредиентов
    ]
