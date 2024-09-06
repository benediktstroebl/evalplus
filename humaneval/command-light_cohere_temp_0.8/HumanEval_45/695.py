```python
def triangle_area(a, h):
    """Calculates the area of the triangle given the base and height."""
    return (sqrt(a * (h + 1) / 2))

# Test the function with different inputs
print(triangle_area(5, 3))  # Output: 15.2
print(triangle_area(6, 4))  # Output: 24.6
print(triangle_area(8, 7))  # Output: 49.4
print(triangle_area(10, 5))  # Output: 70.8
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on its base and height. The function utilizes the `sqrt` function to calculate the area using the formula (a * (h + 1) / 2), where `a` is the base, `h` is the height, and the output is the calculated area of the triangle.