Here is a Python script that contains a self-contained function to calculate the area of the triangle:
```python
import math
def triangle_area(a, h):
    area = 0.5 * math.sqrt(a + h)
    return area
```

This script defines a function named `triangle_area` that calculates the area of the triangle using the formula for the area of a triangle. The function then accepts two arguments: the length of the base side `a` and the height of the triangle `h`.