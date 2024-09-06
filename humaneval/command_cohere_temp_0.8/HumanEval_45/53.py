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
    
    return 0.5 * a * h
```

The function `triangle_area` calculates the area of a triangle given the length of a side `a` and its height `h` using the formula `0.5 * a * h`. The script also includes a test that checks if the function returns the expected value for example inputs `a=5` and `h=3`.

To run the test, you can call the function with the input values `a=5` and `h=3` and compare the returned area with the expected value `7.5`.