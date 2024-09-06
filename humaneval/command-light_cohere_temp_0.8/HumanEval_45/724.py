```python
def triangle_area(a, h):
    """Calculate the area of the triangle."""
    return (sqrt(a * (h + 1) / 2)) ** 2

# Unit tests
assert triangle_area(5, 3) == 7.5
assert triangle_area(8, 6) == 56.25
assert triangle_area(4, 4) == 16
```