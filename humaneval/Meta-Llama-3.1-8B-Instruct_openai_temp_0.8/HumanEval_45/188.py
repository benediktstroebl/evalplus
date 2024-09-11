### Calculating the Area of a Triangle

Below is a Python function that calculates the area of a triangle given the length of one side and its corresponding height.

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of one side of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side length and height must be positive.")
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This function uses the formula for the area of a triangle which is `(base * height) / 2`. It checks for invalid input (i.e., when either the side length or the height is non-positive), and raises a `ValueError` in such cases.