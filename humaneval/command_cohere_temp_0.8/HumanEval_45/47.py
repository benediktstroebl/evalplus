```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can simply provide the length of a side and the height of the triangle as shown in the docstring. The function calculates the area using the formula 0.5 * base * height and returns the result.  This approach takes into account that the given side length is the base of the triangle, and then calculates the area using the height as the perpendicular distance from the base to the opposite vertex. This is a common approach for calculating the area of a triangle when you know the base and height.