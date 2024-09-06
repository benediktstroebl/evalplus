```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The function first checks whether the sum of the sides is substantially different from each side's length. If so, it returns -1, implying the sides cannot form a triangle. Otherwise, it employs Heron's formula to compute the area and rounds it to two decimal places.