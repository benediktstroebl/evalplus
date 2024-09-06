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

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs opposing the side. This formula is used to calculate the area of triangles with known sides.

This Python function, `triangle_area`, takes in two arguments, `a` and `h`, representing the side length and height of a triangle, respectively. It initially validates that both inputs are positive values, throwing a `ValueError` if either is non-positive. It then calculates the area using the formula and returns the area as a floating-point number. 

Here is an example usage of the function:
```python
>>> triangle_area(5, 3)
7.5
```
This will return the area of the triangle if the side length is 5 and the height is 3.