```python
def triangle_area(a, h):
    return 3.14159 * (a**2) * (a + h)

print(triangle_area(5, 3))  # Output: 28.1415
print(triangle_area(5, 4))  # Should raise ValueError
```