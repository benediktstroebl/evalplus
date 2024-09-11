```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The formula used is: Area = 0.5 * base * height
    
    Args:
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

This script defines a function `triangle_area` that takes two arguments, `a` and `h`, which are the base and height of a triangle, respectively. It returns the area of the triangle using the formula `0.5 * base * height`. The script also includes a test case to demonstrate how to use the function.