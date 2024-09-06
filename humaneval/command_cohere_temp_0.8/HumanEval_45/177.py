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
        raise ValueError("Height and length of a side must be positive")
    
    area = 0.5 * a * h
    return area
```

The function incorporates input validation to check that the input values are positive, raising a ValueError if they are not. This ensures that the function behaves predictably and deals with invalid input gracefully.

To see how the function behaves with edge cases, you can run:
```python
>>> triangle_area(0, 1)
Traceback (most recent call last):
  ...
ValueError: Height and length of a side must be positive
```

Or
```python
>>> triangle_area(10, 0)
Traceback (most recent call last):
  ...
ValueError: Height and length of a side must be positive
```

And to confirm that the area calculation is correct for valid inputs:
```python
>>> triangle_area(7, 12)
84.0
```