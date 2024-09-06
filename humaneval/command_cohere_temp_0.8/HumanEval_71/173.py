```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
```
The provided code defines a Python function called `triangle_area` that estimates the area of a triangle when given its three side lengths as arguments. The function first checks whether the sum of the side lengths violates the triangle inequality principle, which would indicate that the sides do not form a valid triangle. It does this by computing the sum of the side lengths and comparing it to each individual side length, disregarding very small differences due to floating-point errors. If the condition holds true, indicating a valid triangle, the function employs Heron's formula to calculate the area using the side lengths. Finally, the calculated area is rounded to two decimal places before being returned, and -1 is returned otherwise.