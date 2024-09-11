```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    
    The formula used is: area = (base * height) / 2
    
    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height should be positive numbers.")
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))
print(triangle_area(0, 3))  # Test for invalid input
```

This script defines a function `triangle_area` that takes the length of the base (`a`) and the height (`h`) of a triangle as input, and returns the area of the triangle. The function uses the formula `area = (base * height) / 2` to calculate the area. It also includes a check to ensure that both the base and the height are positive numbers. If either of them is not, it raises a `ValueError` with a corresponding message. The script includes an example usage of the function, including a test case for invalid input.