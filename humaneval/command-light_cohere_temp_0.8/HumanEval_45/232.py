Here's a self-contained Python script that defines a function triangle_area and solves the problem for a triangle with given sides:
```python
import math
def triangle_area(a, h):
    return math.sqrt(a**2 + h**2 - math.sqrt(3))
```

This script defines a function `triangle_area` that takes two arguments, `a` and `h`. The function returns the area of the triangle with the given side length and height, using the formula for the area of a triangle.