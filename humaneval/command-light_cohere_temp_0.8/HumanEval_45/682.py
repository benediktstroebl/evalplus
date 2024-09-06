```python
def triangle_area(a, h):
    return 3.14159 * 8 / (a**2 + h**2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5  # #

# Test with edge cases
 assert triangle_area(0, 0) == 0
 assert triangle_area(1, 1) == 1.0  #

# Test with random values within range
 assert triangle_area(-2, 5) == 4.14159 * 8  # #
```

This Python code defines a function `triangle_area` that calculates the area of a triangle with given sides `a` and `h`, using the formula for the area of a triangle. It also defines a function `test_triangle_area` that tests the `triangle_area` function with a variety of inputs, including edge cases and random values within a specified range.