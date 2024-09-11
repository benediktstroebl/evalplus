```python
def triangle_area(a, h):
    """
    Returns the area of a triangle given its base (a) and height (h).
    
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 5))  # Output: 25.0
```

This Python function takes two arguments: `a`, which is the length of the base of the triangle, and `h`, which is the height of the triangle. It returns the area of the triangle using the formula for the area of a triangle: `Area = 0.5 * base * height`. The function is also tested with two example use cases.