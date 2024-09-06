```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return round(area, 2)
```

The function follows the prompt instructions to determine whether the three sides form a valid triangle, using summation to test the condition. If the sides form a valid triangle, it calculates the area and returns it rounded to two decimal places. Otherwise, it returns -1.