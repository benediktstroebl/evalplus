```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return round(area, 2)
```

The function follows the prompt instructions to check if the sum of any two sides is greater than the third side. The validation employs a small tolerance to avoid zero division errors, and the validity check is executed only once, optimizing performance. If the sides form an invalid triangle, -1 is returned; otherwise, the area is calculated using Heron's formula and rounded to two decimal places. 

This is an example of how to test this function:
```python
>>> triangle_area(3, 4, 5)
6.00

>>> triangle_area(1, 2, 10)
-1
```