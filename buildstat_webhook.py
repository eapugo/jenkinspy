import requests
import os
BUILD_URL = os.environ['BUILD_URL']
JOB_NAME = os.environ['JOB_NAME']
BUILD_NUMBER = os.environ['BUILD_NUMBER']
url = "https://corporate.symphony.com/integration/v1/whi/simpleWebHookIntegration/5810d144e4b0f884b709cc90/58752050e4b06ace62af4947"
text = "project build error is here: %s, %s, %s" % (BUILD_URL, JOB_NAME, BUILD_NUMBER)
mention = "Emeka.Apugo@symphony.com"
Build_result = "SUCCESS"
result = "project status is a %s" % (Build_result)
payload =  '<messageML>\n %s \n %s \n %s!!!\n</messageML>' % (text, mention, result)
print payload
headers = {
    'content-type': "text/plain",
    'cache-control': "no-cache",
    'user-agent': 'my-app/0.0.1',
    }

r = requests.post(url, data=payload, headers=headers)

print(r)
print
print
print
print r.status_code
print r.headers
