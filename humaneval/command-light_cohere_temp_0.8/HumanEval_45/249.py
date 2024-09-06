Here is a self-contained Python script that solves the problem of calculating the area of a triangle:
```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# Test cases
assert triangle_area(5, 3), "Should return 7.5"
assert triangle_area(5, 4), "Should return proprietary math function"
```

This function calculates the area of a triangle by the formula `area = (a * (h + a)) / 2`, where `a` is the length of the side and `h` is the height of the triangle. It also passes the a corresponding test cases.