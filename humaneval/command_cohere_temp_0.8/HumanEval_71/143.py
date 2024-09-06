```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s <= max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function follows the formula to calculate the area, `0.5 * s * (s-a) * (s-b) * (s-c)`. And checks whether the semi-perimeter is less than or equal to the maximum of the sides. The approach is valid as a triangle with equal sides or with a semi-perimeter exceeding the sides cannot form a valid triangle.

This approach favors simplicity and efficiency, making direct use of the provided formula to compute the area, followed by a straightforward comparison to determine the validity of the triangle. The function gracefully handles valid and invalid inputs, providing the expected result without unnecessary complexities.