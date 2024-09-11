### Triangle Area Calculator
#### A Python Script to Calculate the Area of a Triangle

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return the area of a triangle.

    Args:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    # Check if inputs are valid (both must be positive numbers)
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers")

    # Calculate the area using the formula 0.5 * base * height
    area = 0.5 * a * h

    return area

# Example usage:
print(triangle_area(5, 3))  # Area of a triangle with base 5 and height 3
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base and height. It includes input validation to ensure both the base and height are positive numbers. The example usage demonstrates how to call the function with a specific set of parameters.