Here's a self-contained Python function that calculates and returns the area of a triangle given its three sides:

```python
import math

def triangle_area(a, b, c):
    return math.sqrt((a** * (b**2 + c**2 - a**2) / 2) * math.sqrt(2))
```

This function takes three sides of the triangle as input and returns the area of the triangle. The function uses the area formula, which is the sum of the squares of the opposite sides of the triangle.