```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called `triangle_area` that calculates the area of an triangles when given the lengths of its three sides. It first checks whether the sum of the sides constitutes a valid triangle. If the sum is not close to any of the sides, indicating that the sides cannot form a valid triangle, it returns -1. However, if the sides do form a valid triangle, it employs the Heron's formula to compute the area using the three sides, with the result rounded to two decimal places and returned as the output.