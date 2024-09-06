```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    # Using the formula for triangle area from Heron's Formula: area = 0.5 * a * h
    return 0.5 * a * h
```

This function `triangle_area` takes two arguments, `a` and `h`, and returns the area of the triangle based on the formula. Note that this approach assumes that the given side `a` is the base of the triangle and the height `h` is perpendicular to the base.