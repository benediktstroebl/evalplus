```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
This function calculates the area of a triangle when given the three sides `a`, `b`, and `c`. It first checks whether the sum of the two largest sides is greater than the smallest side in absolute value. If this condition is not met, it returns `-1` to indicate that the sides do not form a valid triangle. If the condition is met, it proceeds to calculate the area using the Heron's formula and rounds the result to two decimal places before returning it.