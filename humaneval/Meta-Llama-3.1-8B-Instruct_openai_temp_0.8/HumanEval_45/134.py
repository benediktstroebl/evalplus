### Calculating the Area of a Triangle
#### Using the Formula: Area = 0.5 * base * height

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height, return area for a triangle.

    Args:
        a (float): Length of the base of the triangle.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```

This Python script defines a function `triangle_area` that takes two arguments: `a` for the base of the triangle and `h` for the height. It returns the area of the triangle using the formula `Area = 0.5 * base * height`. The example usage demonstrates how to call the function with a base of 5 and a height of 3, and prints the resulting area.