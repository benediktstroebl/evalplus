```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)), 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by comparing the sum of any two sides to the third side. If the triangle is not valid, the function returns -1. If the triangle is valid, it calculates the area using the formula `0.5 * (s * (s-a-b) * (s-a-c) * (s-b-c))`, where `s` is the sum of the side lengths, and rounds the result to two decimal places before returning it.

This solution is designed to provide a clear and concise way to determine the area of a triangle given its side lengths, while also checking for validity.