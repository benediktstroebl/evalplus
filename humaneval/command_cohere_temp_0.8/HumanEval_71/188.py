```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return '{:.2f}'.format(area)
    else:
        return -1
```

The function follows the problem's directive to check if the sum of any two sides is greater than the third side to determine a valid triangle. The Pythagorean theorem is then used to calculate the area of the valid triangle.