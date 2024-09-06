```python
def triangle_area(a, h):
    return 3.14 * (a** * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5, "Assertion failed: (5,3) = 7.5"

test_triangle_area() # Passes the test successfully
```