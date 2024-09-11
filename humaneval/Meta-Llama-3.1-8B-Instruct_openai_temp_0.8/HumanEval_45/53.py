```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    Parameters:
    a (float): length of a side
    h (float): height of the triangle
    
    Returns:
    float: area of the triangle
    
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of a side `a` and the height `h`. The function uses the formula for the area of a triangle, which is `(base * height) / 2`. In this case, the base is the length of the side `a`.

The script also includes a docstring that explains the purpose of the function, its parameters, and its return value. Additionally, it includes a test of the function by calling it with the values `5` and `3`, and printing the result.

You can save this script to a file (e.g. `triangle_area.py`) and run it from the command line using `python triangle_area.py` to see the result.