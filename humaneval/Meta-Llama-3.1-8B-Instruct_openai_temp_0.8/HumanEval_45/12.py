### Triangle Area Calculator
#### A Python Script to Calculate the Area of a Triangle
### Given the Length of a Side and the Height

```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side and the height. It returns the calculated area. The example usage at the end demonstrates how to use this function.