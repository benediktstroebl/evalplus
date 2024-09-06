```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
The provided code defines a Python function called `triangle_area` that calculates the area of an invalid triangle with side lengths `a`, `b`, and `c` and returns -1 if the sides do not form a valid triangle according to the specified criteria. It checks if the sum of any two sides is greater than the length of the third side to validate the triangle. If the sides form a valid triangle, it calculates the area using the Heron's formula and rounds the result to two decimal places.