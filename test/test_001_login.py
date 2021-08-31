import requests
import json

host_url = 'http://3.142.29.177/api/login'

headers= {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  }

body = {
    "email": "valinesoft@gmail.com",
    "password": "valinesoft",
}

response_code = requests.post(host_url, headers=headers, data=json.dumps(body))

print('Response of this POST call is')
print(response_code.status_code)
response_data = response_code.json()
print(response_data['data']['token'])
