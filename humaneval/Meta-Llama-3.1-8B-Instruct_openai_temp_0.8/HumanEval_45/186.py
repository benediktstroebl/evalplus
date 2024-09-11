```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.
    
    The area of a triangle is given by the formula:
    area = 0.5 * base * height
    
    :param a: The length of the base of the triangle.
    :type a: float
    :param h: The height of the triangle.
    :type h: float
    :return: The area of the triangle.
    :rtype: float
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive")
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base and height. It also includes a docstring with information about the function and its parameters. If either the base or height is not positive, it raises a ValueError.