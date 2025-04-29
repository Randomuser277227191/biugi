import requests

def get_snapchat_user_id(handle):
    url = f'https://app.snapchat.com/web/api/v2/getUserByUsernameOrId?username={handle}'
    response = requests.get(url)
    data = response.json()
    return data['user']['id']

def get_snapchat_ip_address(user_id):
    url = f'https://feelinsonice-hrd.appspot.com/web/deeplink/snapcode?username={user_id}&type=SIMPLE'
    response = requests.get(url)
    return response.json()['snapMap']['bitmoji']['location']['ipAddress']

def main():
    handle = 'example_username'  # Replace with the actual Snapchat username
    user_id = get_snapchat_user_id(handle)
    ip_address = get_snapchat_ip_address(user_id)
    print(f'IP address associated with Snapchat handle {handle}: {ip_address}')

if __name__ == '__main__':
    main()