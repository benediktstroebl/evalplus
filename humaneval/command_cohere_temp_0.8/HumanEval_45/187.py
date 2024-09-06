```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle. 
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    triangle_area = (a * h) / 2  # Simplified formula for area of a triangle
    return triangle_area
```

The formula for the area of a triangle is `${\text{Area}} = \frac{{{\text{base length}} \cdot {\text{height}}}}{2}$. In the above code, the function `triangle_area()` takes in two parameters, `a` for the length of the side and `h` for the height. It then calculates the area using the formula and returns the area of the triangle. 

This function is self-contained and can be imported and used independently without relying on any external variables or functions.  It also provides an example of how to use the function within the function docstrings, which is a good practice to make your code more readable and usable by following the principle of informative documentation.