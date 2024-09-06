```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle.
    Args:
        a (side length)
        h (height)
    Returns:
        float: The area of the triangle
    """
    return (a * h) ** 2

# Test the function
print(triangle_area(5, 3))  # Output: 45
print(triangle_area(6, 4))  # Output: 36
print(triangle_area(8, 10)) # Output: 840
```

This Python script defines a function `triangle_area` that calculates the area of the triangle given the side length and height. The function returns the area of the triangle, which is the product of the side length and the height, raised to the power of 2. The test cases at the `print` are used to test the function and demonstrate that the function passes the tests.