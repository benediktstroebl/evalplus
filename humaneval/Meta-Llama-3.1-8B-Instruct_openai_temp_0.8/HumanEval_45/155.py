### Calculating the Area of a Triangle
#### Using the Formula: Area = (base * height) / 2

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return area for a triangle.

    Parameters:
    a (float): Length of the base of the triangle.
    h (float): Height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise ValueError("Both base and height must be numbers")
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive")
    
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the base `a` and the height `h` of a triangle as input and returns its area. The area is calculated using the formula `(base * height) / 2`. It includes input validation to ensure that both the base and height are positive numbers.