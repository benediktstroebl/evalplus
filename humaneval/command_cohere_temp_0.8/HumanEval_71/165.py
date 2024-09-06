```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - a) > 1e-9 and abs(s - b) > 1e-9 and abs(s - c) > 1e-9:
        area = (a * b * (c / s)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function assesses the condition of a valid triangle with the given lengths of the three sides. If the condition is met, it calculates the area of the triangle using the Heronian formula and rounds the result to two decimal places. If the sides don't form a valid triangle, it returns -1.