```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    """
    return 0.5 * a * h
```
The function `triangle_area()` calculates the area of a triangle using the formula `0.5 * a * h`, where `a` is the length of a side and `h` is the height. This area formula is particularly applicable to triangles where the height is perpendicular to the base (side)`a`. 

This formula can be proven using the following three steps:
1. Sum the triangle's three rectangles whose areas are `a*h`, `a*h` and `a*h` respectively.
2. Sum the three rectangles of areas `a*h`, `0*h` and `0*h` respectively.
3. Summing the areas of the above two triangles and divide them by 2.

Thus, the average value of the areas of these triangles is `0.5*a*h`.