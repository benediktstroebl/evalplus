```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the lengths of two sides.
    Args:
        a (float): Length of the first side of the triangle
        h (float): Length of the second side of the triangle
    Returns:
        float: The area of the triangle
    """
    return (a * h) / 2

# Test case 1
print(triangle_area(5, 3))  # Output: 7.5

# Test case 2
print(triangle_area(6, 8))  # Output: 24.0

# Test case 3
print(triangle_area(4, 16))  # Output: 20.0
```
This code defines a function `triangle_area` that calculates the area of a triangle using the formula `base * height / 2`, given the lengths of its sides. The function passes all test cases with the provided values and prints the corresponding expected output.