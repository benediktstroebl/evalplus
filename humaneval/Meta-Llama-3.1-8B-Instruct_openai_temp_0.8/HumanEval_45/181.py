```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): The base length of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function called `triangle_area` that takes two arguments, `a` and `h`, which represent the base length and the height of a triangle respectively. It calculates the area of the triangle using the formula `0.5 * base * height` and returns this value. The script then tests this function with a sample input.