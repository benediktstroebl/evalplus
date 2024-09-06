Here is a Python script that defines a function triangle_area that calculates and returns the area of a triangle given the lengths of its sides:
```python
import math

def triangle_area(a, b, c):
    """Calculate the area of a triangle.
    return math.sqrt((b**2 * *a + (c - a))**2)

# Unit tests
def test_triangle_area():
    assert triangle_area(5, 3, 4) == 7.5
    assert triangle_area(10, 5, 6) == 6.8
    assert triangle_area(4, 5, 7) == 11.0
```
This script defines a function `triangle_area` that takes the three sides of a triangle as arguments, and returns the area of the triangle using the formula `sqrt((b-a)*(b-c)**. The script also includes a unit test to ensure the function works correctly.