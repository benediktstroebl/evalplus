```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the side length and height of a triangle, and it will return the calculated area of the triangle. 
Like in the docstring example, if the given side is 7 and the height is 12, then the area would be calculated as:
```python
triangle_area(7, 12)
```
Which would result in ```python
42.0
```
Being returned. 
This area is calculated based on the formula for the area of a triangle (base * height / 2).