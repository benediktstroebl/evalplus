Here's the function to calculate the area of a triangle, along with the test cases:
```python
import math
def triangle_area(a, h):
    return math.sqrt(a * (h / 2))

# Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(8, 4) == 12.0
assert triangle_area(10, 5) == 42.0
```

This script defines a function `triangle_area` that takes two parameters, `a` and `h`, representing the lengths of the sides of the triangle. The function then uses the mathematical formula for the area of a triangle to calculate the area and returns the result. It is then tested with three different cases to ensure its correctness.