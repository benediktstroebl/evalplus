```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(6, 2) == 12.0

# Test case 3
assert triangle_area(8, 4) == 40.0

# Test case 4
try:
    assert triangle_area(-5, 3) is None
except AssertionError:
    print('Case is not valid')
```