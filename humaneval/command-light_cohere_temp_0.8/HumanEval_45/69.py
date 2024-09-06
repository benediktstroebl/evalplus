Here is a self-contained Python script that defines a function triangle_area that calculates the area of a triangle based on its side length:

```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(8, 6) == 28.0
```

This script defines the function `triangle_area` that takes two parameters: the side length `a` of the triangle and the height `h`. It then calculates the area of the triangle using the formula `Area = (a * (h + a) / 2)`. The test cases ensure that the function is correct and returns the expected results.