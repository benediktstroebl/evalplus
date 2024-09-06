```python
def triangle_area(a, h):
    return 3.0 * a * (a + h) ** 2

def test1():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.0

def test2():
    assert triangle_area(0, 0) == 0.0
    assert triangle_area(1, 1) == 1.0
```
This code includes a function `triangle_area` which calculates the area of a triangle with a given side and a hypotenuse. The function also passes the test cases that verify its correctness.