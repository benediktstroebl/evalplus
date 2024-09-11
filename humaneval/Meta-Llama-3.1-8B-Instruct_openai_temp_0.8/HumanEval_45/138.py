```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The length of the side of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) of a triangle as input, calculates the area using the formula `0.5 * a * h`, and returns the result. The example usage at the end demonstrates how to use this function with the provided example inputs.