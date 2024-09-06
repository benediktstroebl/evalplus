```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called `triangle_area` that estimates the area of a triangle based on its side lengths. The function takes three arguments, `a`, `b`, and `c`, representing the lengths of the triangle's sides. It starts by calculating the sum of these side lengths, storing the result in the variable `s`. Then it checks if the sum of any two of the sides is sufficiently different from the remaining side length to qualify as a valid triangle according to the problem statement. If the conditions for a valid triangle are met, it calculates the area using the Heron's formula `(1/4) * sqrt(s * (s-a) * (s-b) * (s-c))` and rounds the result to two decimal places before returning it. Otherwise, it returns -1 to indicate that the side lengths do not form a valid triangle.