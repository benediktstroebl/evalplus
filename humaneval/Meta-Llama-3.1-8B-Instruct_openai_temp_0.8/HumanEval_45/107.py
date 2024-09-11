```python
def triangle_area(a, h):
    """Given length of a side (base) and high return area for a triangle.
    The area of the triangle is calculated by the formula: area = (base * height) / 2
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("The length of a side and the height must be positive.")
    area = (a * h) / 2
    return area

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) of a triangle as arguments, and returns the area of the triangle. The area is calculated using the formula `area = (base * height) / 2`. If either `a` or `h` is non-positive, the function raises a `ValueError`. The script also includes an example usage of the function.