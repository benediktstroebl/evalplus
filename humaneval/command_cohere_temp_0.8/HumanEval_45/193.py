```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Note: The height is the distance between the side with length a and the opposite vertex.
    """
    return 0.5 * a * h
```
The function avoids assumptions about the side lengths of the triangle and defines useful core concepts in commenting for understanding. 

To employ this function just call it with the relevant side length and height, e.g.:
```python
>>> triangle_area(5, 3)
7.5
```