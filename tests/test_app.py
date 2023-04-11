from .. import app

def test_hello():
    test = app.MyClass()
    assert test.hello() == 'hello world!'