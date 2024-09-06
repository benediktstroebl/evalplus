```python
def triangle_area(a, h):
    return 3.14 * a *a * (h + a) ** 2

#Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(10, 6) == 42.0
```

The code defines a function called `triangle_area` that calculates the area of the triangle using the formula for the area of a triangle. The function takes two parameters: the length of one side (`a`) and the height of the triangle (`h`). 

The code then tests the `triangle_area` function with two different sets of parameters and verifies if the returned area matches the expected result using the provided tests.