```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): The base of the triangle.
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

This script defines a function `triangle_area` that calculates the area of a triangle given its base (`a`) and height (`h`). It uses the formula for the area of a triangle (`0.5 * base * height`) to compute the result. The example in the docstring demonstrates how to use the function and the print statement at the end tests it with the example given in the problem statement.