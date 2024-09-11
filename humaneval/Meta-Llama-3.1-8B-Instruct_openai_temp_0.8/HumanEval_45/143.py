```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula used is (base * height) / 2. In this case, the base is 'a' and the height is 'h'.

    Args:
        a (float): The length of the side of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    area = (a * h) / 2
    return area

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given the length of one side and the height. It uses the formula for the area of a triangle, which is `(base * height) / 2`, where the base is 'a' and the height is 'h'. The function is then tested with the example given in the problem statement.