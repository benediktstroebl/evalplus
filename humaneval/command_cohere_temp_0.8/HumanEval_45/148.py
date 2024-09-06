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
        raise ValueError("Height and side length must be positive")
    
    return 0.5 * a * h
```

The function incorporates input validation to check that the input values are positive, raising a ValueError if they're not. It then calculates the area using the formula `area = 0.5 * a * h`.

To test this, you can call the function with various inputs. Here's an example:
```python
>> triangle_area(7, 5)
17.0
```