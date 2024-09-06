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
    return 0.5 * a * h
```

This function calculates the area of a triangle using the formula `0.5 * a * h1`, where `a` is the length of the side and `h` is the height or length of the triangle. It incorporates a usage example within the function that verifies the function behavior against expected output. The example argument values of `5` and `3` result in a returned area of `7.5` which is echoed in the double-quoted string that follows the `Example` keyword.