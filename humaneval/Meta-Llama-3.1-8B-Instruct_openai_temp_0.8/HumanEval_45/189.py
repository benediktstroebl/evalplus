### Calculating Triangle Area
#### Formula: (base * height) / 2

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2
```

You can run this script in your Python environment to test the `triangle_area` function. Just call the function with two arguments (the base and height of the triangle) and print the result.