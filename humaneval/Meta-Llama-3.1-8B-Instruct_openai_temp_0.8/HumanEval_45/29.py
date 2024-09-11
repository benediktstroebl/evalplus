```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The formula used is: area = 0.5 * base * height
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. It raises a `ValueError` if either the base or the height is non-positive, as this would not form a valid triangle. The script then tests the function with two example inputs.