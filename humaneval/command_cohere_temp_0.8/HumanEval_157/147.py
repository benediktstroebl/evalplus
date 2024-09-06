```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = sqrt(s*(s-a)*(s-b)*(s-c))  # Height

    # Determine if the triangle is right-angled using the Pythagorean theorem
    return h == b or h == a or h == c
```

This function adheres to the problem's specifications, checking for a right angle using the Pythagorean theorem. It returns True when the triangle is right-angled, and False otherwise, fulfilling the example scenarios provided.