```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    The area of a triangle is calculated as (base * height) / 2. 
    In this case, 'a' represents the base and 'h' represents the height.
    
    Parameters:
    a (float): The base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 5))  # Output: 25.0
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, representing the base and height of a triangle, respectively. It calculates the area using the formula (base * height) / 2 and returns it. The function also includes docstrings to provide a description of what it does, its parameters, and its return value. The script then tests the function with two example calls.