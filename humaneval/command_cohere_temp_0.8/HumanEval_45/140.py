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

The function returns 0 if the height is zero to handle the edge case and provides an example in the documentation. It returns half the product of the length of a side `a` and the height `h` of the triangle. This formula should work for triangles with sides less than 90 degrees. 

To follow the best practices, the requirements and returns should be clear, and the function should have appropriate comments and a good readable name.

If you need help with more code reviews or require help writing tests, please let me know!