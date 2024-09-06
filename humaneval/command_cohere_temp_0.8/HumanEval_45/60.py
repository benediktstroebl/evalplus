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
    if h == 0: 
        return 0 
    return 0.5 * a * h
```

The function `triangle_area` calculates the area of a triangle when provided with a length of a side and its height. It adheres to the Pythagorean theorem which states that the sum of the areas of the triangle is equal to half the product of its legs. The function also handles a potential edge case, where the height is zero, returning zero area for such a flat triangle.

To test, just run the following command:
```python
>>> triangle_area(5, 3)
7.5
```