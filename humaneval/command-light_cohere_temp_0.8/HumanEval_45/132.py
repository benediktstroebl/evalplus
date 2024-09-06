```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

# Tests
print(triangle_area(5, 3))  # Should print 28.125
print(triangle_area(3, 5))  # Should print 12.5
print(triangle_area(-5, 3))  # Should raise ValueError
```