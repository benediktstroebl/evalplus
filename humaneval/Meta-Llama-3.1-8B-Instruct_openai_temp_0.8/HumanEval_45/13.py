```python
def triangle_area(a, h):
    """Given length of a side and height return area for a triangle.
    
    Args:
        a (float): Length of the base of the triangle.
        h (float): Height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Testing the function
print(triangle_area(5, 3))  # Output: 7.5
```

This Python script defines a function `triangle_area` that calculates the area of a triangle given its base length `a` and height `h`. The function takes two arguments, `a` and `h`, and returns their product divided by 2. The script also includes a docstring that provides information about the function, its arguments, return value, and an example usage. Finally, it tests the function with the example provided in the problem.