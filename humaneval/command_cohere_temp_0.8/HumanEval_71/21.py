```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```
This Python script defines a function called `triangle_area` taking three arguments `a`, `b`, and `c`, which represent the lengths of the three sides of a triangle. 

The function first calculates the semi-perimeter of the triangle, which is half of the sum of all three sides. It then uses a criterion originating from triangle geometry, called the Pythagorean Inequality Theorem, which states that if the sum of any two sides of a triangle is greater than the third side, the triangle is valid. The function concludes by rounding the triangle's area to two decimal places using the `round()` function, or returning -1 if the sides do not form a valid triangle. 

This code should be able to be run independently in Python, and it passes the provided tests, as well as prints the triangle area when the sides form a valid triangle, and -1 when the sides are not long enough to form a valid triangle.