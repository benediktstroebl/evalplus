```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    Formula used: Area = (base * height) / 2
                 Since it's a triangle, we consider one of the sides as base.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
print(triangle_area(10, 5))  # Expected output: 25.0
```

This script defines a function `triangle_area` that takes two parameters: `a` (the length of a side) and `h` (the height). It returns the area of the triangle according to the formula `Area = (base * height) / 2`. The script then tests this function with two example use cases.