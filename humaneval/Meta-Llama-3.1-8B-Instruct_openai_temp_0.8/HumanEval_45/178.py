### Self-Contained Python Script for Calculating Triangle Area
```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): length of a side
    h (float): height of the triangle
    
    Returns:
    float: area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```
This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) as input parameters and returns the area of the triangle. The area is calculated using the formula `0.5 * a * h`. The script also includes a test case to demonstrate the function's usage.