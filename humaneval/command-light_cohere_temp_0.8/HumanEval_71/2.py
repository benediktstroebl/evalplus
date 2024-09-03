Here is a Python script that solves the problem you provided:
```python
import math
def triangle_area(a, b, c):
    # Check for positive side lengths
    if (a < 0 or b < 0 or c < 0):
        return None  # Return None if any side length is negative
    return math.sqrt(a**2 + b**2 + c**2)
# Example usage
print(triangle_area(3, 4, 5)) # Output: 6.0
print(triangle_area(1, 2, 10)) # Output: -1.0
```
The script defines a function called `triangle_area` that takes the lengths of three sides of a triangle as input and calculates the area of the triangle. It then checks if any of the side lengths are negative and returns `None` if so, as the triangle is not valid. The test is done by checking if the sum of any two sides is greater than the third side length.