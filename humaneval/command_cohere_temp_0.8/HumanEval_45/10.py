```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if h <= 0 or a <= 0:
        raise ValueError("Height and side length must be positive numbers.")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or distance between the side and the base. This formula is included in the docstring of the function for future reference.

The function includes input validation to check that both `a` and `h` are positive numbers. If they are not, a `ValueError` is raised. This helps ensure that the function is called with valid inputs and provides a clear error message when it is not.

The example usage at the end demonstrates how the function is called with valid inputs, and the area of a triangle is calculated. It also serves to demonstrate the behavior of the function for these specific inputs.