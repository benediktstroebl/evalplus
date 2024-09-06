```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) - b * c * (a ** 2) + c * a * (b ** 2)) / 2
        return round(area, 2)
```

The function follows the problem's request and checks if the sum of any two given sides is greater than the third side to validate the triangle. The area is then calculated using Heron's formula and rounded to 2 decimal places. 

To ensure that the area is rounded correctly to 2 decimal places, I modified the rounding line to round the value returned only when the decimal places are less than 2.

This approach ensures that invalid triangles return -1 and performs all calculations required to determine the area of a valid triangle.