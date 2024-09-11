```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The formula used is: area = 0.5 * base * height
    >>> triangle_area(5, 3)
    7.5
    """
    # validate inputs
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive")
    
    area = 0.5 * a * h
    return area

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. It includes input validation to ensure both `a` and `h` are positive numbers. If either input is invalid, it raises a `ValueError`. Finally, it provides an example usage of the function.