```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    The area of a triangle is calculated using the formula: area = (base * height) / 2
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be greater than zero")
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
```

This script defines a function `triangle_area` that takes the base `a` and height `h` of a triangle as arguments and returns its area. It includes a docstring that describes the function's purpose and behavior, as well as example usage. The function also includes input validation to ensure that the base and height are greater than zero.