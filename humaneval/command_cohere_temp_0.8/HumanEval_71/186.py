```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(s) * (s - min(s)) ** 0.5) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's spec regarding to the rules of a valid triangle and also outputs the area rounded to two decimal places. 

The logic behind the calculation is the Heron's formula which states that the area of a triangle can be calculated as the square root of the product of the semi-perimeter and the maximum side length, divided by 2.