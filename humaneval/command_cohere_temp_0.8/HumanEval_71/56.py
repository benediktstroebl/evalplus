```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - a) > 1e-9 and abs(s - b) > 1e-9 and abs(s - c) > 1e-9:
        area = (a * b * (c * (c - a - b) / (2 * s))).round(2)
    else:
        area = -1
    return area
```

The function takes in three numbers representing the sides of a triangle and determines whether the sides form a valid triangle based on the condition that the sum of any two sides is greater than the third side. The area is then calculated using the formula for a triangle's area and rounded to two decimal places. If the sides do not form a valid triangle, the function returns -1.