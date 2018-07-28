import requests
import json

#Set API paths
api_url_base = 'https://api.pushshift.io'
comment_endpoint = '/reddit/comment/search'
post_endpoint = '/reddit/submission/search'
subreddit_endpoint = '/reddit/subreddit/search'

#Set request headers
headers = {'Content-Type': 'application/json'}

def get_request(endpoint, parameters):
    api_url = '{0}{1}'.format(api_url_base, endpoint)

    response = requests.get(api_url, headers = headers, params = parameters)

    if not response_error_parse(response):
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def response_error_parse(response):
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
    elif response.status_code == 404:
        print('[!] [{0}] URL not found'.format(response.status_code))
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
    elif response.status_code == 200:
        print('Request Good!')
        return False
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return True


if __name__ == "__main__":
    params = {'sort':'asc'}
    random_comments = get_request(comment_endpoint, params)
    if random_comments is not None:
        print('Here\'s your info: ')
        i = 0
        for item in random_comments['data']:
            i+=1
            print('\nItem {0}'.format(i))
            for k, v in item.items():
                print('{0}:{1}'.format(k, v))
    else:
        print('[!] Request Failed')