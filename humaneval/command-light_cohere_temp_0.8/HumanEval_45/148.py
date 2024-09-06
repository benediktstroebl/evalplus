```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return sqrt((a*h) / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(6, 12) == 42

# Test case 3
try:
    print(triangle_area(0, 0))
except ZeroDivisionError:
    print("Error: Cannot calculate area with zero length.")
```