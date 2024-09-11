```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Parameters:
    a (float): length of side
    h (float): height of triangle
    
    Returns:
    float: area of triangle
    
    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate area using the formula: area = 0.5 * base * height
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). The formula used for this calculation is `0.5 * base * height`. The function includes a docstring that provides a description, parameters, return value, and examples of usage. The script then tests this function with the example case from the problem statement.