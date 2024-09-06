```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return '{:.2f}'.format(area) if area >= 0 else -1
    else:
        return -1
```

The function outputs the area of the triangle when the sum of any two sides is greater than the third side. If not, the function returns -1.