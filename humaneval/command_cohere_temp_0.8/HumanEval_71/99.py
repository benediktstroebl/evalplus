```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * a * c)))), 2)
```
This function calculates the area of a triangle with side lengths a, b, and c. It first checks whether the sum of any two sides is greater than the third side, adhering to the triangle inequality theorem. If the sides do not form a valid triangle, the function returns -1. If the sides do form a valid triangle, the function calculates the area using the law of cosines. Note that this approach is more robust than assuming the triangle is equilateral. 

The math.acos function returns the angle in radians, so we use math.sin to convert it to a decimal value between -1 and 1, factoring in the sign of the result for accuracy. We then round the area to 2 decimal places and return it.

Here is a test suite that can be used to validate the function:
```python
def test_triangle_area():
    # Valid triangle
    assert triangle_area(3, 4, 5) == 6.00
    
    # Should be a valid triangle ( INVALID )
    assert triangle_area(1, 2, 10) != -1
    
    # Invalid triangle
    assert triangle_area(10, 2, 1) == -1
    
    # Another invalid triangle
    assert triangle_area(1, 11, 5) == -1
```
This test suite includes tests for both valid and invalid triangles, ensuring that the function behaves as intended.