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
    
    area = 0.5 * a * h
    return area
```

The function takes two arguments, 'a' representing the length of a side of the triangle and 'h' representing the height of the triangle. It then calculates the area using the formula `0.5 * a * h` . This formula is based on the fact that the area of a triangle is equal to half of the product of its base and height. 

To handle edge cases, the function includes checks to validate input. It checks if both `a` and `h` are larger than zero and raises a `ValueError` if either input is less than or equal to zero. This helps prevent errors and provides clearer guidance to users about valid inputs. 

Lastly, the function is also documented with a simple example that shows how the function can be invoked and explains the expected output.  This helps users understand how to use the function and the kind of result they can expect.