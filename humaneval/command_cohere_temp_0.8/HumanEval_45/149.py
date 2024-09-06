```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    Output units are 2D Euclidean space.
    
    Args:
    - a (float): Length of side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle a and h.
    """
    return 0.5 * a * h
```

This function calculates the area of a triangle using the formula `0.5 * a * h`, where `a` is the length of a side and `h` is the height. This Area formula is derived from the formula for the area of a triangle using the base and height of a triangle. 

To validate the functionality of the function, you can test it with different inputs to verify that it returns the expected results. For example:
```python
>>> triangle_area(5, 3)
7.5
>>> triangle_area(10, 5)
25
```