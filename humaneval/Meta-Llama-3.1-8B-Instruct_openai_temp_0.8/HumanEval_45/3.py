### Calculating the Area of a Triangle
```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula used is: area = (base * height) / 2

    Args:
        a (float): The length of the base side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```
In this script, the `triangle_area` function calculates the area of a triangle given the base length (`a`) and the height (`h`). It uses the formula `area = (base * height) / 2` to calculate the area. The function is then tested with the example input values.