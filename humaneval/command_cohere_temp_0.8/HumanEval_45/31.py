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
    if h == 0:  # Divide by zero prevention
        return "Height of the triangle cannot be zero"
    return 0.5 * a * h
```

This function calculates the area of a triangle when given one side's length and the height. It is important to note that the function incorporates a precaution against division by zero, checking if the height is zero. In this case, the function returns a message indicating that the height is inappropriate.

To test this function, try calling it with different inputs, such as the example provided in the docstring, comparable cases, and edge behavior testing (e.g., side length equals zero, negative number).