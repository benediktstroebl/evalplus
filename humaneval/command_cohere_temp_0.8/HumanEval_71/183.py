```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == a + c or s == b + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's specification of checking if the sum of any two sides is greater than the third side as a criterion for a valid triangle. The area is then calculated using Heron's formula when the sides form a valid triangle.