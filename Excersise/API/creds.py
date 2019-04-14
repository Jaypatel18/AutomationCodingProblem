import requests

def wrong_cred(input):

    user = input[0]
    passw = input[1]

    url = "https://api.shipt.com/auth/v2/oauth/token?white_label_key=shipt"

    head={
        'X-User-Type' : 'Customer',
        'Content-Type' : 'application/x-www-form-urlencoded'
    }

    wrong_data = {
        "username" : user,
        "password": passw,
        "grant_type" : "name"
    }

    paramater = {
        "white_label_key" : "shipt"
    }

    output1 = requests.post(url, header=head, params = paramtaer, data=wrong_data)

    print("Output : ", results.text)

    if output1.status_code == 401:
        return output1.json()['error']['message']
