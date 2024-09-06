Here is a sample Python script that contains a self-contained function to calculate the area of a triangle:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(3, 4) == 6.25
assert triangle_area(10, 5) == 50

```
This script defines a function `triangle_area` that calculates the area of a triangle using the formula `(a * (h + a) / 2)`. The function is then tested with various input values, and the results are compared against the expected values using the `assert` assert statement.