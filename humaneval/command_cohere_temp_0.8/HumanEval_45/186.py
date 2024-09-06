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
        raise ValueError("Height and length of a side must be positive values.")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of the side and `h` is the height. This formula is used to calculate the area of a triangle when you know the length of a side and the height.

This script includes test examples that validate the functionality of the `triangle_area()` function.

To run the code locally, copy and paste the script into a Python environment of your choice. You can run the tests using the `unittest` module by calling `unittest [module]`. In this case, running `unittest triangle_area` will run the tests.