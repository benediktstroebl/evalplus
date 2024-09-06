```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
The provided code defines a Python function called `triangle_area` that calculates the area of an triangles when given its three side lengths as arguments. It first checks if the sum of any two sides is greater than the third side, which is the condition for a valid triangle. If the sides do not form a valid triangle, it returns -1. Otherwise, it calculates the area using the Heron's formula and rounds the result to two decimal places before returning.