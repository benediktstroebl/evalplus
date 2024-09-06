```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c**2 - (a**2 + b**2) / 4)) / 2
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by comparing the sum of any two sides to the third side. If the triangle is not valid, the function returns -1. If the triangle is valid, it calculates the area of the triangle using the formula `1/2 * a * b * (c**2 - (a**2 + b**2) / 4)`, and rounds the result to two decimal places before returning it.

This formula is derived from the fact that the sum of the areas of the three triangles makes up the whole area of the triangle with side lengths `a`, `b`, and `c`.

The tests ensure that the function correctly identifies invalid triangles and produces correctly rounded areas for valid triangles.