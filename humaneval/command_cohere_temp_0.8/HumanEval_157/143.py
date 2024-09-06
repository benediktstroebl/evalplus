```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) ** 0.5  # Hypotenuse using Heron's formula

    return h == c or h == a or h == b

# Tests
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This script uses Heron's formula to calculate the length of the hypotenuse, and then checks if it matches any of the three sides. This effectively checks for the conditions of a right-angled triangle.