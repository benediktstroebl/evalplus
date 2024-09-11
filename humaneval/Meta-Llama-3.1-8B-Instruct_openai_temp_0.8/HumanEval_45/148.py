```python
def triangle_area(a, h):
    """
    Given length of a side (the base) and height, 
    returns the area for a triangle.

    The formula used is:
    area = (base * height) / 2

    :param a: Length of the side (the base)
    :param h: Height of the triangle
    :return: The area of the triangle
    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage
print(triangle_area(5, 3))
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, representing the length of the side (the base) and the height of a triangle, respectively. It calculates the area of the triangle using the formula `area = (base * height) / 2` and returns the result. The example usage at the end shows how to use this function to calculate the area of a triangle with base length 5 and height 3.