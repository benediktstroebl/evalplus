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

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height or length of the triangle's legs opposing the side of length `a`. This formula is used to calculate the area of triangles with perpendicular legs. This script ensures that both inputs are positive numbers and raises a `ValueError` if they are not.

To use this script, save it as a `.py` file (e.g., `triangle_area.py`). You can then run the script from the command line or import the function into another Python script.