```python
def triangle_area(a, h):
    return 3 * a * (h + a)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(10, 5) == 50

# Test case 3
try:
    value = triangle_area(15, 12)
except AssertionError as e:
    print(f"Error: {e}" )
```