```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle when given the lengths of its three sides (a, b, and c). The function first checks whether the sum of any two sides is sufficiently larger than the third side to form a valid triangle. If the conditions for a valid triangle are met, the function calculates the area using the formula `((a*b)*sqrt(3))/2` and rounds the result to two decimal places before returning it. If the sides cannot form a valid triangle, the function returns -1.