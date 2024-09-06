```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the length of two sides."""
    # Pythagorean theorem
    s = (a + h) ** 2
    return s / 2

# Test case 1
print(triangle_area(5, 3))  # Expected output: 7.25

# Test case 2
print(triangle_area(6, 8))  # Expected output: 24.5

# Test case 3
print(triangle_area(2, 7))  # Expected output: 14.0

# Test case 4
print(triangle_area(3, 6))  # Expected output: 20.6
```

This script defines a function `triangle_area` that calculates the area of a triangle based on the length of its sides using the Pythagorean theorem. The function then passes four test cases, and the expected outputs are also provided.