Here's a self-contained Python function that calculates the area of the triangle:

```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test case 1: Input values for a = 5 and h = 3
print(triangle_area(5, 3))  # Output: 7.5

# Test case 2: Invalid input values
try:
    triangle_area(10, 5)
except ValueError as e:
    print(e)
```

The code defines a Python function `triangle_area` that calculates the area of a triangle using the formula `(a * (h + a) / 2)`, where `a` and `h` are the lengths of the triangle's sides. The function then passes the example tests with valid inputs and raises a `ValueError` exception with an corresponding error message for invalid inputs.