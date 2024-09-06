```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c))**, 2)
```
The function first checks whether the sum of the sides is different from each of the sides by more than 1e-6, which is effectively 0. This is a small number placed to ensure that all the almost-zero differences return valid triangles. If the sum is significantly different from any side, it returns -1, otherwise it calculates the area and returns it rounded to two decimal places.