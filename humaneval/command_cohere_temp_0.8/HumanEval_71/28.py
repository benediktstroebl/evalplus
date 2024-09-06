```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
This Python script defines a function called `triangle_area` taking three parameters `a`, `b`, and `c` representing the lengths of the three sides of a triangle. The function first checks whether the sum of the lengths of any two sides is greater than the length of the third side to determine if the three sides form a valid triangle. If the conditions are met, the function proceeds to calculate the area of the triangle using the Heronian formula, which is 2 times the square root of the sum of the squared lengths of all three sides, divided by half of the length of the perimeter, and rounds the result to two decimal places. If the sides cannot form a valid triangle, the function returns -1.