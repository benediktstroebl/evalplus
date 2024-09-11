```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    The formula for the area of a triangle is: Area = (base * height) / 2
    
    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(10, 4))  # Output: 20.0
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. It then demonstrates the function's usage with two examples.