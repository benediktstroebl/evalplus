```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    Args:
        a (float): Length of one side of the triangle
        h (float): Height of the triangle
    Returns:
        float: Area of the triangle
    """
    return 0.5 * a * h

# Example usage:
print(triangle_area(5, 3))  # Outputs: 7.5
print(triangle_area(4, 6))  # Outputs: 12.0
```

This script defines a function `triangle_area` that takes the length of one side `a` and the height `h` of a triangle as inputs, and returns their product divided by 2, which is the formula for the area of a triangle. The function includes a docstring to explain its purpose, arguments, and return value, following standard professional guidelines for Python documentation. The script then demonstrates how to use this function with two example calls.