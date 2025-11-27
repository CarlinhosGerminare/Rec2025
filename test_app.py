import requests

def test_hello():
    response = requests.get('http://localhost:3000/')
    assert response.status_code == 200
    assert 'Hello World' in response.text

if __name__ == '__main__':
    test_hello()
    print("Testes passaram!")
