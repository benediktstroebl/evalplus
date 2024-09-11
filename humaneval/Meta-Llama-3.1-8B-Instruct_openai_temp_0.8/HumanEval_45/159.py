```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): The length of a side of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of a side `a` and the height `h`. The area is calculated using the formula for the area of a triangle, which is (base × height) / 2. The base is assumed to be the side `a`, and the height is given by `h`. The function is tested by printing the area of a triangle with a side length of 5 and a height of 3.