```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The formula used is: area = (base * height) / 2.
    For an isosceles triangle, when you're given the length of a side, 
    you can consider it as the base and height of the triangle.
    
    Parameters:
    a (float): The length of a side of the triangle.
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

In this script, we define a function `triangle_area` that takes two parameters, `a` and `h`, which represent the length of a side and the height of the triangle, respectively. The function then returns the area of the triangle using the formula `area = (base * height) / 2`.