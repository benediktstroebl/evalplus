```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    
    Args:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    
    Returns:
    - float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    if h == 0: 
        return 0  # Handle division by zero
    return 0.5 * a * h
```

This function calculates the area of a triangle when given one side's length and the height. It guards against division by zero with a quick check on the height.

To use this code, you can add it to your project and import it locally:
```python
import triangle_area  # Assuming you save this code in a file named triangle_area.py

# Test the function
assert triangle_area(5, 3) == 7.5
```

If you want to test the function without adding the code to a separate file, you can copy and paste it into a Python environment or IDE, which allows you to run individual functions.