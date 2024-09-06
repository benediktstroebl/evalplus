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

The function returns 0 if the height is zero to avoid division by zero and returns 0 otherwise. Additionally, the docstring includes an example that shows how to use the function and provides instructions on how to provide the necessary arguments.