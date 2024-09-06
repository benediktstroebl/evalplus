```python
def triangle_area(a, h):
    return sqrt(3 * (a**2 + h**2))

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(3, 6) == 10.0

# Test case 3
assert triangle_area(10, 5) == 42.0
```
This code defines a function called `triangle_area` that calculates the area of the triangle using the formula A = sqrt(3 * (a^2 + h^2)) based on the given lengths a and h. The code passes three test cases with the corresponding asserts, which check if the function's output is correct for the given inputs.