```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - max(s)) < 1e-5:
        area = (a * b * (c * (c - a - b) / 2)) / 2
        return round(area, 2)
    else:
        return -1
```

The function follows the problem's specification and checks whether the sum of any two of the given sides is greater than the third side to determine a valid triangle. The area is then calculated using Heron's formula when the triangle is valid. The function rounds the result to two decimal places, as per the guidelines. Finally, it returns -1 if the sides do not form a valid triangle.