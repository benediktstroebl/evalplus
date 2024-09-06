```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-6:
        area = (max(s) * (s - min(s)) ** 0.5) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the logic you provided in the original prompt. It first checks whether the sum of the sides is equal to the maximum side length, thereby forming a valid triangle. If the triangle is valid, it calculates the area and rounds it to two decimal places. Otherwise, it returns -1.