### Triangle Area Calculator
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): Length of the base of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2


# Test the function
print(triangle_area(5, 3))
```
This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The area is calculated using the formula `A = (a * h) / 2`, where `A` is the area of the triangle. The script includes a docstring that explains the purpose of the function, its parameters, and its return value. It also includes a test case to demonstrate the function's usage.