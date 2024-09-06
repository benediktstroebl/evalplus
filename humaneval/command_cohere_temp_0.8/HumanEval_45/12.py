```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    
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
        raise ValueError("Height and side length must be positive")
    
    return 0.5 * a * h
```

This function calculates the area of a triangle when given one side's length and the height. It incorporates input validation to ensure that the side length and height are positive values. The area is then computed using the formula `0.5 * a * h`, where `a` represents the side length and `h` represents the height.

Here's an example of how to use this function:
```python
>>> triangle_area(5, 3)
7.5
```

This will return the area of a triangle with a side length of 5 and a height of 3.