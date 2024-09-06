```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 15.5
print(triangle_area(5, 6)) # Should raise ValueError
print(triangle_area(10, 10)) # Should raise ValueError
```