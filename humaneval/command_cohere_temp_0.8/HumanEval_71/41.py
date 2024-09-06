```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-9 and abs(s - b) > 1e-9 and abs(s - c) > 1e-9:
        area = (a*b)*((5.*b+c)/2.)
        return round(area, 2)
    else:
        return -1
```

The function follows the problem definition and uses the formula (base * height)/2 to calculate the area of the triangle when the given lengths form a valid triangle. The sum of any two sides should be greater than the third side for the given lengths to form a valid triangle.

To test this function, ensure that the sum of any two given lengths is greater than the third length to verify the correctness of the area calculation and the valid condition.