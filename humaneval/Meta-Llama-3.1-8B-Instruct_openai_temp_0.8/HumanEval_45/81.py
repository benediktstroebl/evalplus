### Triangle Area Calculator
#### Python Script

```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    The formula for the area of a triangle is:
    area = (base * height) / 2

    In this case, the length of the side (a) is used as the base.

    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.

    Returns:
        float: Area of the triangle.
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, the `triangle_area` function calculates the area of a triangle given the length of a side (`a`) and the height (`h`). The function uses the formula `area = (base * height) / 2` to calculate the area, where the length of the side is used as the base. The script also includes a test case to verify the function works as expected.