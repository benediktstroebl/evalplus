```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Height

    # Verify that the triangle is right-angled
    return h == b or h == c or h == a
```

The function calculates the height of the triangle based on the semi-perimeter theory, checks whether the calculated height matches any of the side lengths, and returns True if it does, indicating a right-angled triangle. It returns False if the height doesn't match any side, ensuring the triangle is not right-angled.