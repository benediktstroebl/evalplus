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
        raise ValueError("Height and length must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of the side and `h` is the height. This formula is used to calculate the area securely. This code also handles negative values and raises a ValueError indicating that the height and length must be positive. 

The code also includes an example in the function signature that shows how to use the function and confirms that the function calculates the area correctly.