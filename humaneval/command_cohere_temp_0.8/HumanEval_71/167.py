```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
The provided code defines a Python function called triangle_area that calculates the area of a triangle when given the lengths of its three sides (a, b, and c). It first checks if the sum of any two sides is greater than the third side, adhering to the triangle inequality theorem. If the sides do not form a valid triangle, it returns -1. Otherwise, it employs Heron's formula to calculate the area using the three side lengths, rounding the result to two decimal places.