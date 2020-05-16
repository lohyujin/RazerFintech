from .. import all_module as am
from .utils import to_d128, deposit

register_bp = am.Blueprint('register', __name__)


@register_bp.route('/register', methods=['POST'])
def register_user():
    data = am.request.get_json()
    if not data:
        return am.jsonify({'msg': 'Bad Request, no data passed'}), 400

    try:
        first = data["first_name"].lower()
        last = data["last_name"].lower()
        email = data["email"].lower()
        username = data["username"]
        password = data['password']

    except KeyError:
        return am.jsonify({'msg': 'Bad Request, missing/misspelled key'}), 400

    dynamodb = am.boto3.client('dynamodb')
    # user = dynamodb.get_item(TableName='login', Key={'username': username})
    pw = am.bcrypt.generate_password_hash(password.encode('UTF-8'))
    dynamodb.put_item(TableName='login', Item={'username':{'S': username},'password_hash':{'B': pw}})

    return am.jsonify({'msg': 'User Registered'}), 201

    # return am.jsonify({'msg': 'Username already exist'}), 409
