```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / 12, 2)
    else:
        return -1
```
This function calculates the area of a triangle when given the lengths of its three sides `a`, `b`, and `c`. It follows these steps:
1. It calculates the semi-perimeter s as the sum of the sides divided by 2.
2. If the semi-perimeter is less than or equal to the largest side, it proceeds to calculate the area.
3. Otherwise, it returns -1 to indicate an invalid triangle.

The area is computed using the Heron's Formula, which provides a straightforward way to calculate the area of a triangle given its sides. This is done by multiplying the semi-perimeter with the differences of each side and then dividing by 2 and 12. The result is then rounded to 2 decimal places. 

This approach is intuitive and easy to understand, requiring only simple arithmetic operations. 

Note: this function assumes that the given lengths are already validated for correctness, such that all three lengths are distinct and positive. If these preconditions are not met, the function may not work as expected.