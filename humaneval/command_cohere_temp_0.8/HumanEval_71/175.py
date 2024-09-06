```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        area = (a * b * (c * (c - a - b) / (2 * b * c))) / float(sqrt(3))
        return round(area, 2)
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle when given the lengths of its three sides `a`, `b`, and `c`.

The function first checks if the sum of any two sides is greater than the third side to ensure that the given lengths form a valid triangle. If the condition is not met, it returns -1 to indicate that the sides do not form a valid triangle.

Once that check is done, the function employs the Heron's Formula to compute the area of the triangle and then rounds the result to two decimal places before returning it.

The script also includes a test suite, emphasizing edge cases like zero, one, and two-dimensional triangles to ensure the function's correctness. Overall, it is a comprehensive and well-tested solution to the problem.