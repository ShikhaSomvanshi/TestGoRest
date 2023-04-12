import requests

def test_get_users_auth():
    url = 'https://gorest.co.in/public/v2/users'
    headers = {'Authorization': 'Bearer fafad1e0cfad7fde47ecf8d14f114a66fd92c08023e08b74e14691097604960c'}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_users_auth_failure():
    url = 'https://gorest.co.in/public/v2/users'
    headers = {'Authorization': 'Bearer gafad1e0cfad7fde47ecf8d14f114a66fd92c08023e08b74e14691097604960c'}    
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_get_user():
    response = requests.get('https://gorest.co.in/public/v2/users/902633')
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    print(response.json())
    assert len(response.json()) > 1

def test_get_user_failure():
    response = requests.get('https://gorest.co.in/public/v2/users/2633')
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert response.status_code == 404


