```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test
print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 6)) # Output: 12.0
print(triangle_area(0, 10)) # Should raise exception
```