### Calculating the Area of a Triangle

Below is a Python script that calculates the area of a triangle given the length of a side and the height:

```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    Parameters:
    a (float): The base (side) length of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```

This script defines a function `triangle_area` that takes two parameters: the base length `a` and the height `h`. The function returns the area of the triangle calculated using the formula `0.5 * base * height`. The example usage shows how to call the function with sample values and print the result.