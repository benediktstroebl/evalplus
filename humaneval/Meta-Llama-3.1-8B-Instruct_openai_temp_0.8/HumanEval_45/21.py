```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    The area of a triangle can be calculated using the formula: Area = (base * height) / 2
    
    Parameters:
    a (float): length of the base of the triangle
    h (float): height of the triangle
    
    Returns:
    float: the area of the triangle
    
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```

However, if you're working with a right-angled triangle where one side is the base and the other is the height, you would use the side given `a` as the base and `h` as the height to calculate the area.