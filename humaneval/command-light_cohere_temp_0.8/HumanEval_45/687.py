```python
def triangle_area(a, h):
    return 5 * (sqrt(a**2 + h**2) / 2)

# Test cases
assertEqual(triangle_area(5, 3), 7.5)
assertEqual(triangle_area(4, 4), 6.25)
assertEqual(triangle_area(6, 8), 28.0)
assertEqual(triangle_area(8, 6), 26.0)
assertEqual(triangle_area(1, 1), 1.0)
assertEqual(triangle_area(9, 10), 98.0)
```

In this script, we have a function `triangle_area` that calculates the area of the triangle using the formula `area = (1/2) * (a^2 + b^2)`, where `a` and `b` are the lengths of the base and height of the triangle, respectively. The `sqrt` function is used to avoid overflow by taking square root of the sum of squared.

We also have a set of test cases to ensure the function is working correctly for a variety of inputs.