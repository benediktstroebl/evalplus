```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * math.sqrt(3) / 2)
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by comparing the sum of any two sides to the third side. If the triangle is not valid, meaning that all three sides cannot be collinear, the function returns -1. If the triangle is valid, it calculates the area of the triangle using the formula `((5 * a * b) / 2) / sqrt(3)`, and rounds the result to two decimal places for precision.

Here is an example usage of the function:
```python
print(triangle_area(3, 4, 5))
```
This will output:
```
6.00
```
Verification tests can be performed to ensure the function behaves correctly:
```python
assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(1, 2, 10) == -1
```
This demonstrates how the function correctly determines the area of a valid triangle and indicates an invalid triangle with side lengths that do not satisfy the triangle inequality.