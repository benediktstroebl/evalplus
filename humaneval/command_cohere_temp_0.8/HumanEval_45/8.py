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
        return 0  # Divide by zero error if height is 0
    return 0.5 * a * h  # Base times height divided by 2
    """
```

The function `triangle_area` calculates the area of a triangle given the length of a side (`a`) and its height (`h`). It minimizes code duplication by defining an example inline test and leverages the docstring convention to document its purpose, arguments, return value, and examples.

To use this function:
1. Save the code into a file (e.g., `triangle.py`).
2. Run it from the command line via `python triangle.py`.
3. Or, import the function into another Python script.