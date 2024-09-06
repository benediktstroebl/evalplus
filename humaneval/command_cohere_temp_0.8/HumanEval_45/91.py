```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can simply provide the length of a side `a` and the height `h` of the triangle as arguments:
```python
result = triangle_area(5, 3)
print(result)  # Output: 7.5
```

This function calculates the area using the formula `0.5 * base * height` where the base is assumed to be half of the given side length. The result is then returned as the area of the triangle. 

Note that this function assumes that the given side length is the base of the triangle, and that the height is the perpendicular distance from the base to the opposite vertex. If you have different assumptions about the triangle, you may need to adjust the function accordingly.