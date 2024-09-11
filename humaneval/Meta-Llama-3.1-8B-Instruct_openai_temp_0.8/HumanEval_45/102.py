```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    The area of a triangle can be calculated using the formula:
    Area = (base × height) / 2

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))  # Expected output: 7.5
```