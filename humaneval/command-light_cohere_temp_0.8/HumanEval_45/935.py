```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test
assert triangle_area(5, 3), "Should be close to 15.5"

assert triangle_area(6, 6), "Should be close to 36"

# Run some code
print(triangle_area(8, 10))
```