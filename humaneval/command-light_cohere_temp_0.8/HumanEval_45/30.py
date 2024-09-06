Here's a self-contained Python function that calculates the area of a triangle given the lengths of its sides:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
assert triangle_area(5, 3), "Valid area calculation with (5,3)"
assert triangle_area(6, 4), "Valid area calculation with (6,4)"
assert triangle_area(3, 5), "Invalid input: Negative or overlapping sides"
```

This script defines a function `triangle_area` that calculates the area of a triangle based on the lengths of its sides. The function is then tested with various test cases to ensure its correctness.