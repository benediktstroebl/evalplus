### Python Script to Calculate Triangle Area
```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given a side length (a) and height (h).

    Args:
    a (float): The length of the side.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    if a <= 0 or h <= 0:
        raise ValueError("Side length and height must be positive numbers")
    area = 0.5 * a * h  # Use the formula for the area of a triangle: 0.5 * base * height
    return area

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```
This script defines a function `triangle_area` that takes the length of a side (`a`) and the height (`h`) of a triangle as input, and returns the area of the triangle. It includes a docstring that explains the purpose of the function, its arguments, and its return value. The script also includes a check to ensure that both the side length and height are positive numbers.