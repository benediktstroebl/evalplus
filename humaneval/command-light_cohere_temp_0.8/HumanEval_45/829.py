```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test
print(triangle_area(5, 3)) # [5 * (3 + 5) / 2] => 15.0
print(triangle_area(6, 4)) # [6 * (4 + 6) / 2] => 24.0
print(triangle_area(10, 15)) # error: [10 * (15 + 10) / 2] => 85.0
```