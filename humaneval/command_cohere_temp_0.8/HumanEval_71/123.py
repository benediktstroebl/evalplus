```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c))**, 2)
```
The function first checks whether the sum of any two sides is greater than the third side and returns -1 if they do not form a valid triangle. Otherwise, it calculates the area using Heron's formula and rounds the result to 2 decimal places.