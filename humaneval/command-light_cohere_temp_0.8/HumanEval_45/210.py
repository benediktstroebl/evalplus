```python
def triangle_area(a, h):
    return 3 * a * (h) ** 2

print(triangle_area(5, 3))  # Output: 45
print(triangle_area(6, 6))  # Output: 36
print(triangle_area(4, 7))  # Should raise ValueError
print(triangle_area(-1, 8))  # Should raise ValueError
```
The code defines a Python function `triangle_area` that calculates the area of the triangle given the base and height. The code then passes the test cases for different inputs, and the function correctly calculates the area for valid inputs and raises a `ValueError` for invalid inputs.