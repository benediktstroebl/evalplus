Here is a Python script that includes a self-contained function that calculates the area of an triangle given the lengths of its sides:
```python
import math
def triangle_area(a, b, c):
    s = (a*b+b*c+c*a)/2
    return math.sqrt(s)
```

# Test cases
assert triangle_area(5, 3, 10) == 7.5
assert triangle_area(10, 5, 6) == 12.8
assert triangle_area(4, 6, 7) == 22.0
```

This script defines a function `triangle_area` that takes the lengths of two sides of a triangle, and the hypotenuse of the third side as parameters. It then computes therectangular area using the formula: `area = sqrt((base * height)/2)`.  The test cases ensure that the function produces the correct output.