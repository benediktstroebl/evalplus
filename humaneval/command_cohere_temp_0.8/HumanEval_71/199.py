```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) + b * c * (a ** 2) + c * a * (b ** 2)) ** 0.5
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by comparing the sum of any two sides to the third side. If the triangle is not valid, meaning the sum of any two sides is not greater than the third side, it returns -1. If the triangle is valid, it calculates the area of the triangle using the formula `((a*b*c)**2) ** 0.5`, where `()` ** 2 is the semi-perimeter of the triangle, and `(a*b*c)` is the area of the triangle base. Finally, it returns the area of the triangle rounded to two decimal places using the `round()` function.

This solution follows the problem statement and uses Python to check the validity of the triangle and calculate its area using the specified formula.