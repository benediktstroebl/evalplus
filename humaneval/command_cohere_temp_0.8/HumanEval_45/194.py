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
    if h == 0: 
        return 0 
    return 0.5 * a * h
```

The function `triangle_area` calculates the area of a triangle when provided with its height and a side length using the formula `area = 0.5 * a * h` where `a` is the length of the side and `h` is the height. It includes a test that checks if the height is zero, in which case it returns `0` considering that it is a special case where the triangle is a line.