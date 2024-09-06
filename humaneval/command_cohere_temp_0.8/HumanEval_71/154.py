```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
```
This approach directly calculates the area of the triangle using the formula `area = (a * b * sqrt(3) / 2)`, and returns `-1` if the sum of the lengths of any two sides is not greater than the length of the third side.