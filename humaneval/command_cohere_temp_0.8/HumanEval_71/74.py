```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) / (6 * s), 2)
```
The provided code defines a Python function called triangle_area that calculates the area of a triangle when given the lengths of its three sides (a, b, and c). The function first checks whether the sum of any two of the side lengths is greater than the third side length. If this condition is not met, indicating that the side lengths do not form a valid triangle, the function returns -1. Otherwise, the code employs the Heron's formula to calculate the area and rounds the result to two decimal places before returning it.