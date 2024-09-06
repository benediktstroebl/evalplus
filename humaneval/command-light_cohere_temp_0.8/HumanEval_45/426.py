```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** 0.5

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
try:
    assert triangle_area(3, 7) == 22.5
except AssertionError:
    print('Test case 2 failed')
```