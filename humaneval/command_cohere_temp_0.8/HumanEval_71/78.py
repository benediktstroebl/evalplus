```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The function first checks whether the sum of the sides is different from each side's value, which would indicate that the sides cannot form a triangle. If this is the case, the function returns -1. If the sum check passes, the function calculates the area and returns it rounded to two decimal places.

Here is a test suite that can be used to validate the function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(5, 12, 13) == 28.99
    
    # Not a valid triangle
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 1, 1) == -1
    assert triangle_area(7, 8, 9) == -1
``` 
This test suite contains three test functions that together cover different cases, both with valid and not-valid triangles.