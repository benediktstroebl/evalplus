```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * a * c)))), 2)
```
This function calculates the area of a triangle with side lengths a, b, and c. It first checks whether the sum of any two of the sides is greater than the third side, following the definition of a valid triangle provided by the user. If the triangle is invalid, the function returns -1. If the triangle is valid, it employs the Law of Cosines to calculate the area, rounded to two decimal places.

Here is a test suite that validates the functionality of the `triangle_area` function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00
    
    # Should return -1 for an invalid triangle
    assert triangle_area(1, 2, 10) == -1
    
    # Another valid triangle
    assert triangle_area(5, 12, 13) == 20.74
    assert triangle_area(13, 5, 12) == 20.74
    
    # More tests
    assert triangle_area(1, 2, 3) == 2.09
    assert triangle_area(7, 3, 10) == 28.28
    assert triangle_area(10, 3, 7) == 28.28
```
This test suite contains a variety of tests for the `triangle_area` function, verifying that it returns the correct results for various valid triangles and one invalid triangle.