```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
The function first checks whether the sum of the sides is different from each of the sides to validate the triangle. If the triangle is invalid, the function returns -1. If the triangle is valid, the function calculates the area and rounds it to two decimal places before returning it. Please note that this code assumes that the given lengths are numeric and do not raise a "TypeError" exception.