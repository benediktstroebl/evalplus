```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): The length of a side.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes in two parameters, `a` (the length of a side) and `h` (the height of the triangle). It returns the area of the triangle using the formula `(base * height) / 2`. The script then tests the function with the example provided.