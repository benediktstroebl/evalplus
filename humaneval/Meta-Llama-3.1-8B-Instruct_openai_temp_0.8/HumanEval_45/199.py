```python
def triangle_area(a, h):
    """
    Given length of a side 'a' and high 'h' return area for a triangle.
    
    The area of a triangle can be calculated by multiplying the base and height, 
    and then dividing by 2. In this case, we use the given side 'a' as the base.
    
    Parameters:
    a (float): The length of a side.
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
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). It uses the formula for the area of a triangle, which is base times height divided by 2. The function includes a docstring with information about its parameters and return value, as well as an example usage. The script also includes a test case that prints the area of a triangle with base 5 and height 3, demonstrating the function's usage.