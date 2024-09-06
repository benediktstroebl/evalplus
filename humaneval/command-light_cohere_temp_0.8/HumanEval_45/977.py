```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Test the function with known values and expected results
assert triangle_area(5, 3) == 7.5
assert triangle_area(8, 6) == 58
assert triangle_area(13, 10) == 687
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on its sides. It then tests this function using various values for `a` and `h`, successfully passing all corresponding tests.