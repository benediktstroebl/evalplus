```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function adheres to the problem's guidelines by determining the area of a valid triangle using the Heron's formula. It then rounds the calculated area to two decimal places for precision. If the sum of any two sides is not greater than the third, the function returns -1, indicating an invalid triangle.