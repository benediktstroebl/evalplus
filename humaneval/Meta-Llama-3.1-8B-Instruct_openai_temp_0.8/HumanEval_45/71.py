### Calculating the Area of a Triangle

Here's a self-contained Python script that defines the `triangle_area` function:
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return the area of a triangle.

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines the `triangle_area` function, which takes the base `a` and height `h` as arguments and returns the area of the triangle. The function includes input validation to ensure that both the base and height are positive numbers. The example usage is included at the bottom for testing purposes.