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
    return 0.5 * a * h
```

This function calculates the area of a triangle using the formula `area = 0.5 * a * h` where `a` is the length of a side and `h` is the height. The formula is a simplification of the `base * height / 2` formula for triangles, where the base can be thought of as half of the triangle's perimeter. 

To prove the correctness of the formula, we can consider the triangle to be an elevation of a parallelogram with the same height and base as the triangle. The area of such a parallelogram is `base * height`, and cutting it into two equal triangles gives us the formula for the triangle's area. 

The script includes an example and a test to ensure the function returns the expected result. You can use this script by calling the `triangle_area()` function with the side length and height as arguments.