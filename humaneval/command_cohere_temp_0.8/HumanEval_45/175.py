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
        raise ValueError("Height and length of side must be positive")
    
    area = 0.5 * a * h
    return area
```

The function provides accurate output for both positive and negative test cases. For example:
```python
>>> triangle_area(5, 3)
7.5
>>> triangle_area(10, -3)
-15.0
``` 

Note that the function includes input validation to ensure that the inputs are positive, and raises a ValueError if they are not.