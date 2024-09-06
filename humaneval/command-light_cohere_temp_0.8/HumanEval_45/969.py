```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Basic tests for triangle_area function
assert triangle_area(5, 3) == 7.5, "Test 1 failed: {}".format()

# Test for positive input
assert triangle_area(10, 5) == 50.0, "Test 2 failed: {}".format()

# Test for negative input
assert triangle_area(-5, 3) == 0.0, "Test 3 failed: {}".format()

# Test for negative area
assert triangle_area(10, -5) == 0, "Test 4 failed: {}".format()
```