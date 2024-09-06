```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Should print 7.5
print(triangle_area(6, 12)) # Should print 89.0
print(triangle_area(10, 5)) # Should print 55.0
print(triangle_area(0, 100)) # Should raise ValueError
```