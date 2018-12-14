import requests


def test_login_valid_login():
    res = requests.post("https://python-qa-training.herokuapp.com/api/auth/login",
                 json={"email": "burinova@lohika.com", "password": "12345678"})
    assert res.status_code == 404


def test_login_invalid_email():
    res = requests.post("https://python-qa-training.herokuapp.com/api/auth/login",
                 json={"email": "nova@lohika.com", "password": "12345678"})
    assert res.status_code == 404


def test_login_invalid_password():
    res = requests.post("https://python-qa-training.herokuapp.com/api/auth/login",
                 json={"email": "hburianova@lohika.com", "password": "678"})
    assert res.status_code == 401
