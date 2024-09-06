```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Height

    # Verify that the triangle is right-angled
    return h == a or h == b or h == c
```

The function calculates the height of the triangle based on the semi-perimeter concept, a common approach for this problem. It then compares the calculated height to each side length, returning True if a right-angle condition is met.

To ensure robustness, you might want to include input validation to handle cases where input values are not integers or negative, which would result in floating point errors or invalid outputs.