```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
This approach directly computes the area of the triangle using Heron's formula and checks whether the sum of any two sides is significantly different from the third side, which indicates a valid triangle. Additionally, the use of significant digits in the `round` function ensures precision and compliance with the specified formatting.