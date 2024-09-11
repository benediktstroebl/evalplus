```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): Length of the base of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, which represent the length of the base and the height of a triangle, respectively. The function returns the area of the triangle using the formula `0.5 * a * h`. The script also includes a docstring that describes the function's purpose, parameters, and return value, and provides a test case to demonstrate the function's usage.