```python
def triangle_area(a, h):
    return 6 * a * (h / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(8, 5) == 40.0

# Test case 3
assert triangle_area(-10, 6) == 0
```
This Python script defines a function `triangle_area` that calculates the area of a triangle with a given side length `a` and height `h`. It then tests the function with different inputs and asserts that the calculated area is correct.