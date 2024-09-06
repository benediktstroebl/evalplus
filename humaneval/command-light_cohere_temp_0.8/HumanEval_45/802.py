```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the base and height."""
    return (sqrt(a ** 2 + h ** 2) / 2)

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.25
print(triangle_area(10, 5))  # Expected output: 52.5
print(triangle_area(1, 10))  # Expected output: invalid input
```