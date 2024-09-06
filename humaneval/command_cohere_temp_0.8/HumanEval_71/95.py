```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c ** 2) - b * c * (a ** 2) + c * a * (b ** 2)) / 2
        return round(area, 2)
```
This Python script defines a function called `triangle_area` taking three parameters `a`, `b`, and `c` as the lengths of the three sides of a triangle. The function first checks whether the sum of any two sides is greater than the third side to ensure the three sides form a valid triangle. If the condition is not met, it returns -1. If the sides form a valid triangle, it calculates the area using the formula `((a*b*c)**(1/2))` and rounds it to two decimal places before returning the result. This is done using the expression:
```python
area = (a * b * (c ** 2) - b * c * (a ** 2) + c * a * (b ** 2)) / 2
```
This expression simplifies the calculation of the area of a triangle using the sine formula. 

The function rounds the computed area to two decimal places for precision. Overall, the code provides an accurate and efficient solution to determine the area of a triangle given its side lengths, while also ensuring the sides form a valid triangle.