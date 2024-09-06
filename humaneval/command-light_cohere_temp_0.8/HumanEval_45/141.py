```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(3, 5) == 6.25

# Test case 3
assert triangle_area(10, 5) == 56.25

# Test case 4
assert triangle_area(-5, 3) == 0
```