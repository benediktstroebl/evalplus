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

The function returns 0 if the height is zero to handle any potential edge cases and returns the area of the triangle using the formula `area = 0.5 * a * h` where `a` is the length of a side and `h` is the height. Note that this assumes the given side is the base of the triangle and that the height is the perpendicular distance from the base to the opposite vertex. 

To better understand the assumed geometry, let's add some additional documentation:
```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle assumed to be perpendicular to the given side.
    
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