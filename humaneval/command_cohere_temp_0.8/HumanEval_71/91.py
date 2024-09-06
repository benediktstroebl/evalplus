```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - a) > 1e-9 and abs(s - b) > 1e-9 and abs(s - c) > 1e-9:
        area = (a * b * (c * (c - a - b) / (2 * s))).round(2)
    else:
        area = -1
    return area
```

The function assesses the validity of the triangle by checking whether the difference between any two sides and the total sum of sides is greater than zero. If the triangle is invalid, the function returns -1. If the triangle is valid, the function employs a formula to calculate the area and rounds it to two decimal places.