```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    The area of a triangle can be calculated by the formula: Area = (base * height) / 2.
    In this case, we assume 'a' is the base and 'h' is the height.
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the length of the base `a` and the height `h` of a triangle as input and returns the area. It also includes a docstring to explain the purpose of the function, its parameters, return value, and an example usage. Finally, it tests the function with the example given in the problem statement.