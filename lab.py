import requests
import requests.auth
import pdb

appkey = u'B0M-ySIMcoJOmA'
secret = u'ZL0nT6xtVhYeE37zRN_AR0ZRv3U'
username = u'alvearian'
password = u'for da labs!'

def get_some_data(username, password, appkey, appsecret):
    client_auth = requests.auth.HTTPBasicAuth(appkey, appsecret)

    post_data = {\
        'grant_type': 'password',\
        'username': username,\
        'password': password,\
    }
    response = requests.post("https://ssl.reddit.com/api/v1/access_token", auth=client_auth, data=post_data)
    
    print(response.json())

    if not 'error' in response.json().keys():
        headers = {"Authorization": "bearer {0}".format(response.json()['access_token']), "User-Agent": "apiTestingUA/1.0 by alvearian"}
        response = requests.get("https://oauth.reddit.com/api/v1/me", headers = headers)
    
    return response

def query_reddit():
    r = get_some_data(username, password, appkey, secret)
    if not 'error' in r.json():
        print(r.json())
    else:
        print("{0}: {1}".format(r.text, r.reason))