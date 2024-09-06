```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test case 1: Correct function
assert triangle_area(5, 3) == 7.5

# Test case 2: Inputs with correct range
try:
    assert triangle_area(1, 100) >= 0
except AssertionError as e:
    print(f"Test case failed: {e}" )
```