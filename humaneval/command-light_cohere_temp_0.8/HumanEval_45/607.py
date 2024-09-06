```python
def triangle_area(a, h):
    return 3.14 * a * a * h 

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Area of triangle is not correct."

def test_multiplication():
    assert triangle_area(5, 3) == 21, "Multiplication of side length and height does not work correctly."

def test_division():
    assert triangle_area(10, 4) == 6, "Division of side length and height does not work correctly."
```