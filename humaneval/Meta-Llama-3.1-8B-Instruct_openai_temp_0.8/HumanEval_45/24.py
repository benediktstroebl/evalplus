### Triangle Area Calculator

Here's a simple Python script that calculates the area of a triangle given its base and height:

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): base length of the triangle
    h (float): height of the triangle
    
    Returns:
    float: area of the triangle
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))
```

In this script, the `triangle_area` function calculates the area of a triangle using the formula: `area = 0.5 * base * height`. The example usage at the end demonstrates how to use this function.