### Triangle Area Calculator

Below is a Python script that defines a function to calculate the area of a triangle given the length of a side and the height.

```markdown
### Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle.
    h (float): Height of the triangle.
    
    Returns:
    float: Area of the triangle.
    
    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a `triangle_area` function that takes two parameters, `a` (the length of a side) and `h` (the height of the triangle). It calculates the area using the formula 0.5 * base * height and returns the result. The example usage at the end demonstrates how to use this function to calculate the area of a triangle with base 5 and height 3. 

You can save this script to a file (e.g. `triangle_area.py`) and run it in your terminal/command prompt using Python (e.g. `python triangle_area.py`).