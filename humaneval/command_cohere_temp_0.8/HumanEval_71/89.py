```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return '{:.2f}'.format(area)
    else:
        return -1
```

The function `triangle_area` calculates the area of a triangle if the sum of any two sides is greater than the third side. The formula for calculating the area of a triangle using the semi-perimeter `(s)` is `(square root of (s * (s-a) * (s-b) * (s-c))). squared units)`

It returns the area of the triangle rounded to 2 decimal places if the three sides form a valid triangle, otherwise, it returns -1.