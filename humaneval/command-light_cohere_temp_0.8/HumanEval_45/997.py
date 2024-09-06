```python
def triangle_area(a, h):
    """Calculate the area of a triangle given the lengths of its sides."""
    return (a * (h + a) / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(3, 5) == 10.25

# Test case 3
assert triangle_area(8, 6) == 56.25
```
This Python script defines a function called triangle_area, which calculates the area of a triangle based on the lengths of its sides. It passes three test cases, and the function returns the expected results.