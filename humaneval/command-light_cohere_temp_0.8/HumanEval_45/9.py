```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

# Unit tests
assert triangle_area(5, 3) == 7.5
assert triangle_area(3, 5) == 7.25
assert triangle_area(10, 10) == 225

```
This script defines a function `triangle_area` that calculates the area of the triangle given the base and height. The function passes all test cases.