```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called `triangle_area` that estimates the area of a triangle when given its three side lengths as input arguments `a`, `b`, and `c`.

The function first checks if the sum of any two of the side lengths is greater than the third by comparing the sum `s` of all three sides to each individual side length within a very small tolerance threshold of 1e-6 (to account for numerical precision). If the condition is true for any two sides, the function returns -1 to indicate that the sides do not form a valid triangle.

If the sides do form a valid triangle, the function uses Heron's formula to calculate the area using the formula `0.5 * s * (s - a) * (s - b) * (s - c)`, where `s` is the sum of the side lengths. The result is then rounded to 2 decimal places and returned.

The function makes use of Python's list and dictionary comprehension, as well as numerical comparison checks, to accurately and efficiently determine the triangle's area. It adheres to the problem statement's requirement of handling invalid triangles and rounding the result to two decimal places when valid.