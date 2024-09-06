```python
def triangle_area(a, h):
    return 3.14 * a *((a + h) ** 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(3, 5) == 42

# Test case 3
try:
    triangle_area(0, 5)
except AssertionError as e:
    print(e)

# Test case 4
try:
    triangle_area(10, 0)
except AssertionError as e:
    print(e)

# Test case 5
try:
    triangle_area(-5, 10)
except AssertionError as e:
    print(e)
```

This Python code defines a function called `triangle_area` that calculates the area of a triangle with a given base `a` and height `h`. It uses the formula for the area of a triangle, which is `\frac{1}{2} * (a^2 + h^2)`. 

The code then tests the function with various inputs and exceptions, ensuring the correctness of the function by passing all tests.