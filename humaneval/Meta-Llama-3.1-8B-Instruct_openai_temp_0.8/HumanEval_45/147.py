### Calculating the Area of a Triangle
Here is a simple Python function that calculates the area of a triangle given the length of one side and its height.

```python
def triangle_area(a, h):
    """
    Calculates the area of a triangle given the length of one side and its height.

    Args:
        a (float): The length of one side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both side length and height must be positive.")

    # The formula for the area of a triangle is (base * height) / 2
    area = (a * h) / 2
    return area

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This function first checks if the input values are valid (i.e., both side length and height must be positive). Then, it uses the formula for the area of a triangle to calculate the result. The example usage at the end shows how to call the function with specific values and print the result.