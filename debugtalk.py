
import time
import requests

def sleep(n_secs):
    time.sleep(n_secs)

# def get_mtx_session():
#     session = requests.session()
#     url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'
#     headers = {'X-Requested-With': 'XMLHttpRequest'}
#     data = {'accounts': 'Apple2020', 'pwd': '123456'}
#     session.post(url, data=data, headers=headers)
#     return session
# def get_pay_url(jump_url):
#         session = get_mtx_session()
#         resp = session.get(jump_url,allow_redirects=False)
#         pay_url = resp.headers['location']
#         pay_url = pay_url.replace('http://121.42.15.146:9090/','')
#         return pay_url
def get_pay_url1(url):
        url = url.replace('http://121.42.15.146:9090/','')
        return url