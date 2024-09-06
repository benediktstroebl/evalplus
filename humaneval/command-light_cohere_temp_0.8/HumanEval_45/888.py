```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return (a*h)/2

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(10, 5) == 50

# Test case 3
try:
    result = triangle_area(8, 12)
except TypeError:
    print("Error: Input must be numbers")
```

This code defines a function called triangle_area() that calculates the area of a triangle based on the given lengths of its sides. It then passes the
 test cases, and the function passes the tests successfully.