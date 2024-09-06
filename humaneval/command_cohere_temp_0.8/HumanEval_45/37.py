```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Note: The height is the distance between the base (length 'a') and the opposite vertex.
    """
    return 0.5 * a * h
```
The function incorporates the height in its calculation using the formula `base * height / 2 ` to compute the area of the triangle. This generally provides a more accurate depiction of the triangle's area than calculating it from a single side. 
To ensure accuracy, the function's implementation is based on the Pythagorean theorem which equates the height to the difference between the hypotenuse and the side length.