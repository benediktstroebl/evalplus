```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Args:
        a (float): The length of the side.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
assert triangle_area(5, 3) == 7.5
print("All tests passed!")
```

This script defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The area is calculated using the formula `0.5 * base * height`. The script also includes a test case to ensure the function works as expected.