```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
The provided code defines a Python function called triangle_area that calculates the area of a triangle given its three side lengths a, b, and c. It first checks whether the sum of any two of the side lengths is greater than the third side length to ensure that the sides form a valid triangle. If the conditions for a valid triangle are not met, it returns -1. Otherwise, it employs the Heron's formula to compute the area using the three side lengths, with adjustments for numerical precision. The calculated area is then rounded to two decimal places and returned.