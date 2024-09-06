Here is a Python script that includes a self-contained function that solves the problem of finding the area of an triangle with two sides:
```python
import math
def triangle_area(a, h):
    """
    Calculates the area of a triangle given the base and height.
    Args:
    a: float, length of the first side
    h: float, length of the second side
    Returns: float, area of the triangle
    """
    return math.sqrt(0.5 * (a * h) -