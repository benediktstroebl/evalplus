```python
def triangle_area(a, h):
    return 3.14159 * (a ** (h**2) / 2)

# Test
assert triangle_area(5, 3) == 7.5, "Failed to calculate area"
```

This code defines a function called `triangle_area` that calculates the area of the triangle with the given side length `a` and hypotenuse `h`. The test case passes the function with the parameters `5` and `3`, and verifies if the calculated area matches the expected value.