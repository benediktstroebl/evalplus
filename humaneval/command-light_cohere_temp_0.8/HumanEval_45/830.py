```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test
test_passes = triangle_area(5, 3) == 7.5
print(test_passes)
```