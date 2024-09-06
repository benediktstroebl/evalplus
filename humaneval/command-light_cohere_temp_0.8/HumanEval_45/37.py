```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3))  # Should print: 15.5
print(triangle_area(6, 6))  # Should print: 32.0
print(triangle_area(4, 8))  # Should raise TypeError
```