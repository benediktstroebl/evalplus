### Calculating the Area of a Triangle

The area of a triangle can be calculated using the formula: `Area = (base * height) / 2`. 

Below is a Python script that implements this formula:

```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Args:
    a (float): The length of a side of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script includes a docstring that explains how to use the `triangle_area` function, along with an example usage at the end.