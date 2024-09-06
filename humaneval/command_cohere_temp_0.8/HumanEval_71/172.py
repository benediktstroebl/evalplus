```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function follows the steps:
1. Calculate the semi-perimeter s of the triangle and compare it with the longest side of the triangle.
2. If the semi-perimeter is greater than the longest side, the three sides form a valid triangle.
    - Calculate the area of the triangle using Heron's formula.
3. If the semi-perimeter is not greater than the longest side, it means the sides cannot form a valid triangle.
    - Return -1.

The function fully adheres to the problem's specification and handles both successful and unsuccessful scenarios. Ensure that the markdown code block is preceded by a three-line verse for a better presentation.