### Calculating Triangle Area

Below is a Python script that calculates the area of a triangle given the length of a side and its height.

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
    a (float): Length of the side.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script uses the formula for the area of a triangle, which is `A = (base * height) / 2`. In this case, the base is represented by `a` and the height is represented by `h`. The function `triangle_area` takes two arguments, calculates the area using the formula, and returns the result. The test at the end ensures that the function works as expected.