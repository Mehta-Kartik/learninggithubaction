from src.math_operations import add,subtract

def test_add():
    assert add(2,3)==5
    assert add(3,3)==6

def test_subtract():
    assert subtract(4,2)==2
    assert subtract(4,-2)==6
    assert subtract(-4,2)==-6
    assert subtract(3,2)==1