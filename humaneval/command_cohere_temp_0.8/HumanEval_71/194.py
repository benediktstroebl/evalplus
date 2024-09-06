```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * math.sin(math.pi / 3)), 2)
```
The provided code defines a Python function called `triangle_area` that calculates the area of an equilateral triangle when given the lengths of its three sides `a`, `b`, and `c`. The function first checks whether the sum of any two sides is sufficiently different from the length of the third side to qualify as a valid triangle according to the problem statement. If the sides do not form a valid triangle, the function returns -1. Otherwise, it calculates the area of the equilateral triangle using the formula 0.5 * (a * b * math.sin(math.pi / 3)), rounds the result to two decimal places, and returns the rounded value as the area of the triangle.