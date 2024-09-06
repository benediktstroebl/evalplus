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
    if h == 0:  # Divide by zero prevention
        return 0
    return 0.5 * a * h
```

This function calculates the area of a triangle when given one side's length and the height. It is important to note that the function incorporates a division-by-zero prevention mechanism, accounting for scenarios where the height is undefined. The function returns zero in such cases.

To use this function, simply import it within your Python script or Jupyter Notebook:
```python
from functions import triangle_area
```

You can then apply it to compute the area of a triangle using side length `a` and height `h`:
```python
area = triangle_area(5, 3)
print(area)  # Output: 7.5
```

This command will exhibit the area of the triangle, yielding an output of 7.5 in this example.