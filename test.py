import app
import randoms
def test_add():
    assert app.add(2, 3) == 5, "Sum is incorrect"

def test_add1():
    assert app.add(10, 5) == 15

def test_random():
    assert randoms.generate_number() <= 1, "Incorrect condition"

