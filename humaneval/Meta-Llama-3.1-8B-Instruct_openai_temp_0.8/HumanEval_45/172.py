### Calculating Triangle Area
#### Self-contained Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    Args:
        a (float): Length of the side of the triangle.
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

This Python script defines a function `triangle_area` that calculates the area of a triangle given the length of its side `a` and its height `h`. The formula used is `0.5 * base * height`, which is the standard formula for the area of a triangle. The script also includes an example usage to demonstrate how to use the `triangle_area` function.