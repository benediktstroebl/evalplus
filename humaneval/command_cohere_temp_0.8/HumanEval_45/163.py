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

The function includes inputs and outputs validation to ensure that the inputs are positive numbers, and raises a ValueError if they are not. To ensure the output is consistent with the problem statement, the area is calculated using the formula `0.5 * a * h`.

To run the code, you can copy and paste it into a Python environment of your choice. Once executed, the function can be called with any valid input, like `triangle_area(5, 3)` to calculate and return the area of a triangle with a side length of 5 and a height of 3, which should yield an output of 7.5. 

If calling the function with invalid inputs, a ValueError will be raised with an appropriate error message.