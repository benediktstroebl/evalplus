```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Formula for area of a triangle: (base * height) / 2
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the base `a` and height `h`. It uses the formula for the area of a triangle, which is `(base * height) / 2`. The function is then tested with an example usage, where it prints the area of a triangle with a base of 5 and a height of 3.