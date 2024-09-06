```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Note: The height is the distance from the base to the opposite vertex.
    """
    return 0.5 * a * h
```
In this script, the `triangle_area()` function calculates the area of a triangle when given a side length (`a`) and the height (`h`) - the distance from the base to the opposite vertex. Using the formula `Area = 0.5 * a * h`, it then returns the calculated area. This approach considers that the base of the triangle is the side of length `a` and the angle opposite the height `h` is a right angle, resulting in a triangular shape. 

This function can be used to determine the area of any triangle with a given side length and height, enabling practical calculations for geometric applications.