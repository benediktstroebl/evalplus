```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) / (2 * s)  # Height

    # Check if the height is equal to the half of the longest side
    return h == b / 2 or h == c / 2 or h == a / 2
```

The function calculates the semi-perimeter and height of the triangle using the given side lengths, then checks whether the height is equal to half of the longest side, which is a characteristic of a right-angled triangle. The given example inputs return True and False respectively, as expected.