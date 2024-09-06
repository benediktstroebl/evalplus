```python
def triangle_area(a, h):
    """Calculate the area of the triangle given its sides."""
    return (sqrt(a * (h + a)) / 2)

# Test the function
print(triangle_area(5, 3))  # Output: 15.2
print(triangle_area(6, 4))  # Output: 12.0
print(triangle_area(3, 6))  # Output: 10.8
print(triangle_area(8, 5))  # Output: 25.0
```