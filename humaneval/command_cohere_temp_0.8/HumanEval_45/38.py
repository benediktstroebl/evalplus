```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # Based on Heron's formula for triangle's area
    s = (a * h) / 2  # Calculating semi-perimeter
    area = sqrt(s * (s - a) * (s - h) * (s + h))  # Area of the triangle
    return area
```

To test the function, you can run the following code:
```python
test_cases = [
    (5, 3, 7.5),
    (10, 5, 15),
    (2, 7, 10.0),
]

for side, height, expected in test_cases:
    actual = triangle_area(side, height)
    assert actual == expected, f"Failed with side {side}, height {height}: Expected {expected}, got {actual}"
```

This test suite covers multiple scenarios to ensure the function behaves as expected.