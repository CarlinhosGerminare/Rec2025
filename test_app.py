def test_app_imports():
    """Testa se as dependências estão corretas"""
    import flask
    import requests
    print("✅ Dependências OK!")

def test_app_structure():
    """Testa se os arquivos existem"""
    with open('app.py', 'r') as f:
        content = f.read()
        assert 'Flask' in content
    print("✅ Arquivos OK!")

if __name__ == '__main__':
    test_app_imports()
    test_app_structure()
    print("Todos os testes passaram!")
