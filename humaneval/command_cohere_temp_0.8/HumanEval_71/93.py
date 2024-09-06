```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```

The function checks whether the sum of any two of the given sides is greater than the third side. If the condition is met, it calculates the area of the triangle by using Heron's formula and rounds the result to two decimal places. If the sides do not form a valid triangle, the function returns -1.