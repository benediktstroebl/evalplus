```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * sin(pi / 3)), 2)
```
The provided code defines a Python function called triangle_area that calculates the area of an triangles with side lengths a, b, and c. It first checks whether the sum of any two of the sides is sufficiently greater than the third side to form a valid triangle. If the conditions for a valid triangle are met, the code computes the area using the formula half the product of two sides multiplied by the sine of 1/3 of the triangle's internal angle and rounds the result to two decimal places. If the sides cannot form a valid triangle, the function returns -1.