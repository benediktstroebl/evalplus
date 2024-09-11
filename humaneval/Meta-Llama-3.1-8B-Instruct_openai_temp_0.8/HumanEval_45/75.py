```python
def triangle_area(a, h):
    """
    Given length of a side 'a' and high 'h', return area for a triangle.

    The formula used is for the area of a triangle given a side and the height:
    area = (base * height) / 2

    Parameters:
    a (float): Length of a side
    h (float): Height of the triangle

    Returns:
    float: Area of the triangle

    >>> triangle_area(5, 3)
    7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, representing the length of a side and the height of a triangle respectively. It returns the area of the triangle using the formula `area = (base * height) / 2`, where `base` is the length of a side and `height` is the height of the triangle. The example usage demonstrates how to call this function with a side length of 5 and a height of 3, resulting in an area of 7.5.