Here's a self-contained Python function that calculates the area of a triangle with given side lengths:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(10, 6) == 15.0
```
This function calculates the area of a triangle using the formula. It then tests its area formula with the test cases provided.