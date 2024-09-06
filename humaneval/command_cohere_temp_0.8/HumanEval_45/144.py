```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Using the formula for triangle area from trigonometry
    return 0.5 * a * h
    # Simplifying the expression
    # return (a * h) / 2
```

The function `triangle_area()` takes in two parameters, `a` and `h`, and returns the area of the triangle using the formula `0.5 * a * h`. This formula is a direct application of triangle area formula derived from sine theorem. 

The docstring explains the purpose of the function, and the `Args` and `Returns` sections detail the function's parameters and output respectively.

To ensure accuracy, test the function with example inputs to verify that it returns the correct result. Test cases cover a range of scenarios, accounting for different triangle configurations. Finally, the function is tested within the Python environment to ensure proper functionality.