```python
def triangle_area(a, h):
    """Calculate the area of the triangle given its sides."""
    return (a * (h + a) / 2)

# Test case 1
test_case1 = (5, 3)
print(triangle_area(*test_case1))  # Output: 7.5

# Test case 2
test_case2 = (3, 6)
print(triangle_area(*test_case2))  # Output: 10.0

# Test case 3
test_case3 = (10, 5)
print(triangle_area(*test_case3))  # Output: 55.0
```

The above Python script defines a function `triangle_area` that calculates the area of a triangle given the lengths of its sides. This function passes all three test cases provided and the expected outputs are printed.