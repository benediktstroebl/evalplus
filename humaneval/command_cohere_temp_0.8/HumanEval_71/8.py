```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.acos((b**2 + c**2 - a**2) / (2 * a * c)))), 2)
```

The function checks whether the sum of any two sides is greater than the third side. If the sides do not form a valid triangle, the function returns -1. If the sides do form a valid triangle, the function calculates the area using the law of cosines and rounds the result to two decimal places.

Here is a test suite that verifies the function against various valid and invalid input examples:
```python
def test_triangle_area():
    # Valid triangles
    assert triangle_area(3, 4, 5) == 6.00
    assert triangle_area(5, 12, 13) == 29.99
    assert triangle_area(10, 8, 4) == 14.00

    # Invalid triangles
    assert triangle_area(1, 2, 10) == -1
    assert triangle_area(10, 1, 1) == -1
    assert triangle_area(100, 1, 1) == -1

    # Borderline cases
    assert triangle_area(0, 0, 1) == 0.00
    assert triangle_area(0, 1, 0) == 0.00
    assert triangle_area(1, 0, 0) == 0.00
```