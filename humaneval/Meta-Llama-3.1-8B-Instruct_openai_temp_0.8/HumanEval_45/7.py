```python
def triangle_area(a, h):
    """
    Given length of a side (base) and high return area for a triangle.
    
    The formula used is (base * height) / 2.
    
    :param a: Length of a side (base) of the triangle.
    :param h: Height of the triangle.
    :return: The area of the triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Test the function
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that calculates the area of a triangle given the base and height. It uses the formula `(base * height) / 2` to calculate the area. The function includes a docstring that explains its purpose, parameters, and return value. The script also includes a test case to verify that the function works correctly.