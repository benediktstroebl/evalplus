```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test
assert triangle_area(5, 3) == 7.5
assert triangle_area(10, 6) == 35.0
assert triangle_area(1, 10) == 55.0
```