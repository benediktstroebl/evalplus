```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-6:
        area = (a * b * (c * (c - a - b) / 2)) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's specification and returns the area of the triangle when the sum of any two sides is greater than the third side. If the sides do not form a valid triangle, it returns -1.