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
    if h <= 0 or a <= 0:
        raise ValueError("Height and length of a side must be positive")
    
    return 0.5 * a * h
```

The function's logic checks that the input values are positive and then uses the formula `area = 0.5 * a * h` to calculate the triangle's area. It includes a `ValueError` for input validation and a docstring to explain the function's purpose, input, output, and behavior with an example.

To ensure the function behaves as expected, write tests using the `unittest` module. To test the function, do the following:
1. Import the function from the `triangle_area` module.
2. Create test functions within the `unittest` class to validate various scenarios, including negative and zero inputs, as well as inputs that are positive. 
3. Run tests using the `main()` function or directly through the command line via `python -m unittest discover`.

Make sure to have the `unittest` module installed, enable for the script's directory, and run tests to ensure the function's correctness.