### Calculating Triangle Area

The following Python script defines a function `triangle_area` that calculates the area of a triangle given the base length (`a`) and the height (`h`). The area of a triangle is given by the formula: `Area = (base * height) / 2`.

```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The base length of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines the `triangle_area` function with a docstring that explains its purpose, parameters, and return value. It then tests the function with a sample input and prints the result.