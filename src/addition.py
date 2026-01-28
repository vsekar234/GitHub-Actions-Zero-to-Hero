# app.py
# This is a test commits
def add(a, b, c):
    return a + b + c

def test_add():
    assert add(1, 2, 4) == 3
    assert add(1, -1, 5) == 0
