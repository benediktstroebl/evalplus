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
        raise ValueError("Height and length must be positive")
    
    area = 0.5 * a * h
    return area
```

The area of a triangle is calculated using the formula `0.5 * a * h` where `a` is the length of the side and `h` is the height. We return this value if both `a` and `h` are greater than zero. We also validate that both parameters are positive and raise a `ValueError` if they are not. 

To follow best practices, the function starts with an informative docstring that explains what the function does, what the arguments are, and what the return value is. This is invaluable for anyone who might use this function as documentation. The `Example` section shows how to call the function and the value that it returns. It's also informative to include throughout the code snippets that demonstrate how to invoke the function appropriately. 

This is a robust way to write a function and is a good reference for anyone trying to solve problems with code.