import configuration
import requests
import data

def post_new_user(user_body):
    current_body = data.user_body.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body)
def post_new_client_kit(kit_body):
    current_body = data.user_body.copy()
    user_response=requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=current_body)
    auth_token=user_response.json()["authToken"]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }

    current_body = data.kit_body.copy()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=headers)
def get_users_table():
    url = configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    response = requests.get(url)
    return response
