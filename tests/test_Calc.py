from Calculator import Calculator

def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x+y, "add method doesnt work"

def test_subtract():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.subtract() == x-y, "subtract method doesnt work"
