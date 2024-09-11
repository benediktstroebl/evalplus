```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula used to calculate the area of a triangle is:
    Area = 0.5 * base * height
    
    Parameters:
    a (float): Base of the triangle (length of a side)
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, representing the base and height of a triangle, respectively. It returns the area of the triangle, calculated using the formula `0.5 * base * height`. The script then tests the function with an example input and prints the result.