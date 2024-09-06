```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) / 2

# Testing the function with provided inputs
assert triangle_area(5, 3), "Area of triangle is not correct!"

# Another test with different inputs
assert triangle_area(1, 2), "Another incorrect result"
```

The code defines a Python function `triangle_area` that calculates the area of a triangle. It takes the input arguments `a` and `h` for the base and height of the triangle, respectively. The function returns the area, which is the area under the triangle, by multiplying the square of the base and height, then dividing by 2. The function is then tested with two inputs to ensure its correctness.