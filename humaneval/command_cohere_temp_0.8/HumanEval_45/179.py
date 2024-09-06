```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Calculate the area using the formula derived from Heron's formula
    area = 0.5 * a * h
    return area
```

To get the area of a triangle when you know one side and the height, call the function with the side length `a` and the height `h` as arguments like this:
```python
area = triangle_area(5, 3)
```

This will return the area of the triangle with sides of length 5 and a height of 3, which is 7.5 units squared.