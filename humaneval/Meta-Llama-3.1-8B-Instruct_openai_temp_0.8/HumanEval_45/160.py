### Triangle Area Calculator
#### Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula to calculate the area of a triangle is (base * height) / 2.
    In this case, 'a' is considered as the base of the triangle.

    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
print(triangle_area(10, 5))
```

This script defines a function `triangle_area` that takes the base and height of a triangle as input and returns its area. The function uses the formula `area = (base * height) / 2` to calculate the area. The script also includes test cases to demonstrate the function's usage.