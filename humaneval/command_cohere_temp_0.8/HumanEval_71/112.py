```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
The function first checks if the sum of the sides is slightly different from each number. If so, it returns -1 since it is not a valid triangle. Otherwise, it proceeds to calculate the area and rounds it to 2 decimal places before returning it. Please note that this assumes the input is a valid float.