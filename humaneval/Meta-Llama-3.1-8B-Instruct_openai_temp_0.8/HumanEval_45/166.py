```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The formula for the area of a triangle is 0.5 * base * height.
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0:
        raise ValueError("Height must be greater than zero.")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
```

This script defines a function called `triangle_area` that calculates the area of a triangle given its base and height. It checks if the height is greater than zero to ensure that the calculation is valid. If the height is not greater than zero, it raises a `ValueError` with a descriptive message. The script then tests the function with two different sets of inputs.