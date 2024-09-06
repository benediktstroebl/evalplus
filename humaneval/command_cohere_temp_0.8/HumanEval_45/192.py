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
        raise ValueError("Height and side lengths must be positive")
    
    return 0.5 * a * h
```

The function includes inputs (`a`, `h`) and outputs the area of the triangle using the formula `0.5 * a * h`. It also adds diagnostic input/output to verify the function's behavior against its expected behavior as the function's `docstring` includes an example query that tests the function locally.

To ensure the function behaves as expected, you can write additional test cases in the `docstring`, or add a dedicated testing section at the end of the script. Feel free to modify the code to suit your needs or elaborate on any aspect of this solution as needed!