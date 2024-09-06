```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(5, 0)) # Should raise error
```