```python
def triangle_area(a, h):
    """Given length of a base and high return area for a triangle.
    The formula used in this function is (base * height) / 2.
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The function uses the formula `(base * height) / 2` to calculate the area. It also includes a check to ensure that both `a` and `h` are positive numbers, raising a `ValueError` if either is not. Finally, it demonstrates the function's usage with an example.