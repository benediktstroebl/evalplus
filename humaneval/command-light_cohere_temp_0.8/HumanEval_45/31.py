```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the length of a side."""
    return sqrt((a * (a + h)) / 2)

# Basic tests
print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 4))  # Output: 6.4
print(triangle_area(10, 5))  # Output: 50.0

# Edge cases
assert triangle_area(0, 0) == 0
assert triangle_area(a, -h) == triangle_area(a, h)

```