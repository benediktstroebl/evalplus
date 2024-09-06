```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3))  # Should return 7.25
print(triangle_area(5, 4))  # Should return 22.0
print(triangle_area(4, 5))  # Should return 13.0
print(triangle_area(6, 3))  # Should return 52.0
print(triangle_area(-1, 3))  # Should raise error
```