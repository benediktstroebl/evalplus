Here's a self-contained Python script that defines a function `triangle_area` solving the problem:

```python
def triangle_area(a, h):
    return (a*h) / 2

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(5, 6) == 12.0

# Test case 3
assert triangle_area(6, 7) == 23.0
```

This script includes a Python function named `triangle_area` that calculates the area of a triangle with two sides given by `a` and `h`. The test cases ensure that the function's output is correct for various input combinations. 

The `assert` statements are used to pass corresponding tests, and they raise an `AssertionError` if the calculated area does not match the expected value.