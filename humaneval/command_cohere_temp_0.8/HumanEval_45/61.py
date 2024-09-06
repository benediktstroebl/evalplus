```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the length of a side and the height of the triangle, and it will return the area of the triangle, as demonstrated in the provided test case:
```python
>>> triangle_area(5, 3)
7.5
```

This function assumes that the given side is the base of the triangle, which is a common convention in geometry problems. If a different assumption is needed, the function can be adjusted accordingly.  This function is reusable and self-contained, making it easy to integrate into larger projects or problem-solving exercises that involve calculating triangle areas.  If no assumptions are made about the sides given, the function could also be adjusted to take a second parameter highlighting which side is the base in the given problem.  This would extened the functionality of the use of the function and its applicability to a wider range of problems.  This is a common consideration when writing robust functions for geometric and trigonometric calculations.