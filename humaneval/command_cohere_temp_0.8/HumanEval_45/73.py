```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the triangle is a right triangle, the base is half the given side length.
    height = h
    area = 0.5 * base * height
    return area
```

To use this function, you can provide the length of a side and the height, and it will return the area of the corresponding triangle.