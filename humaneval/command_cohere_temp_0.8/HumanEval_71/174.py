```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of any two sides divided by 2. If the semi-perimeter is greater than the longest side, the function calculates the area using Heron's formula. Otherwise, it returns `-1` to indicate that the sides do not form a valid triangle.