```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

In this script, we define a function `triangle_area` that takes two parameters `a` and `h`, representing the base and height of a triangle respectively. It returns the area of the triangle using the formula `0.5 * base * height`. We then test the function with the example provided.