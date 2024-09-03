```python
import math

def triangle_area(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0  # Return 0 if any side length is zero as triangle with zero sides is not valid
    s = (a + b + c) / 2  # Calculate the semi-perimeter
    return math.sqrt(s) * 2  # Return the area of the triangle using the formula for calculating area of a triangle
```

This script defines a function triangle_area that calculates the area of the triangle using the semi-perimeter formula and then returns the result multiplied by 2. The function also includes input validation to handle cases where the triangle is not valid (i.e., when any of its sides is zero).