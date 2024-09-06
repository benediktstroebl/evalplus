```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    Works for triangles of any orientation.
    """
    return 0.5 * a * h
```
The function `triangle_area()` computes the area of a triangle using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height of the triangle. This formula considers the triangular aspect ratio to accurately compute the geometric area irrespective of the triangle's orientation.