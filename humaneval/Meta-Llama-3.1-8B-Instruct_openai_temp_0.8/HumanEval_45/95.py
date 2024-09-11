### Calculating Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    Parameters:
        a (float): Length of the base of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    # Area of a triangle is calculated as 0.5 * base * height
    area = 0.5 * a * h
    return area

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base `a` and height `h`. It returns the calculated area. The example usage demonstrates how to call the function with specific values for `a` and `h` and print the result.