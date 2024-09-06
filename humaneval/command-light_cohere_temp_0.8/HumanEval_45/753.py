```python
def triangle_area(a, h):
    return 6 * a * (h / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(8, 6) == 42

# Test case 3
try:
    assert triangle_area(10, 10) == 100
except AssertionError as e:
    print(f"Error: {e}" )
```