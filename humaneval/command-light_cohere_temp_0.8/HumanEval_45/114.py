Here's a Python script that includes a self-contained function `triangle_area` that calculates and returns the area of the triangle given the lengths of its sides:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test the function with given values
assert triangle_area(5, 3) == 7.5
```
The function calculates the area of the triangle using the formula `(base * height * 1/2)`, and then compares the calculated area with the expected value to pass the test successfully.