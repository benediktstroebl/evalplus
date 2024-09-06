```python
def triangle_area(a, h):
    return 3 * a * (h + a)  # Pythagorean theorem to calculate area

# Test cases
assert triangle_area(5, 3) == 7.25
assert triangle_area(8, 8) == 40.0
assert triangle_area(-5, 3) == error()  # Negative test case
```