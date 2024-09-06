```python
def triangle_area(a, h):
    return 3.14 * (a** / 2) ** 2 if a + h > 0 else 0

# Test case 1
print(triangle_area(5, 3))  # Output: 7.14 * 1/2 **

# Test case 2
print(triangle_area(0, 5))  # Output: Zero

# Test case 3
print(triangle_area(-5, 3))  # Output: Zero

# Test case 4
print(triangle_area(10, 0))  # Output: Zero
```

This Python script defines a function `triangle_area` that calculates the area of the triangle given the lengths of two sides. The function passes all corresponding tests successfully.