```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # The formula for the area of a triangle is 1/2 * base * height
    # Here, we assume the side 'a' is the base of the triangle
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that takes the length of a side `a` and the height `h` as arguments and returns the area of the triangle. The area is calculated using the formula `1/2 * base * height`. The function is then tested with a sample input of `a=5` and `h=3`.