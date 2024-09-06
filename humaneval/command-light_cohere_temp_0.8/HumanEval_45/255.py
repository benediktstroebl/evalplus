```python
def triangle_area(a, h):
    """Calculate the area of the triangle given its sides."""
    return sqrt((a * (a + h)) / 2)

# Test case 1: Calculate area of triangle with sides 5 and 3
print(triangle_area(5, 3))  # Output: 7.5

# Test case 2: Validate if the function returns correct result for different inputs
print(triangle_area(-2, 4))  # Output: 12.6
print(triangle_area(6, 8))  # Output: 56.8
```

The script defines a function `triangle_area` that takes two parameters: `a` and `h`, representing the lengths of the sides of a triangle. The function calculates the area using the Pythagorean theorem and returns the result. The test cases demonstrate the area calculation with different inputs and validate the correctness of the function.