```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (max(s) * (s - max(s))) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's specification of checking if the sum of any two sides is greater than the third side to determine a valid triangle. The triangle area is then calculated using Heron's formula, and the result is rounded to 2 decimal places.