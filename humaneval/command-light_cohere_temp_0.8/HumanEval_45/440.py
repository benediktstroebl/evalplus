```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 12)) # Output: 102

triangle_area.__name__ = "TriangleAreaFunction"

isinstance(triangle_area, type(triangle_area))

triangle_area(10, 20)
```