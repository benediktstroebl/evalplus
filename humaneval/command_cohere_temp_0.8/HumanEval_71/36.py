```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function `triangle_area` calculates the semi-perimeter of the triangle, defined as the sum of the sides divided by two. The semi-perimeter calculates the distance from the center of the triangle to any of its vertices.

The validity of the triangle is then checked by comparing the semi-perimeter with the longest side of the triangle. The condition `s <= max(a, b, c)` checks if the semi-perimeter s is less than or equal to the longest side. If this condition is met, the function proceeds to calculate the area of the triangle using Heron's formula. This formula calculates the area using the lengths of the triangle's sides and the semi-perimeter.

If the triangle is not valid (the semi-perimeter is greater than the longest side), the function returns -1 to indicate an invalid triangle.

The function then uses the `round()` function to round the calculated area to two decimal places for precision.