```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# test cases
assert triangle_area(5, 3), "Should return 7.5 for side 5 and height 3"
assert triangle_area(3, 5), "Should return 6.0 for side 3 and height 5"
assert triangle_area(10, 10), "Should return 351 for side 10 and height 10"
```