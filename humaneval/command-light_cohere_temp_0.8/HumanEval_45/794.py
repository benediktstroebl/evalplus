```python
def triangle_area(a, h):
    return 5 * (a * (h + a)) ** 0.25

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
try:
    print(triangle_area(8, 5))
except AssertionError as e:
    print(e)
```