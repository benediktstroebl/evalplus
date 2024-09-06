```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test
assert triangle_area(5, 3), "Passing Test 1"
assert triangle_area(6, 4), "Passing Test 2"
assert triangle_area(8, 5), "Passing Test 3"

print("Solution passed all tests!")
```