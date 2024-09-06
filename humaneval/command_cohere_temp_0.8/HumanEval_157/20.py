```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    h = (a * b * c) / (2 * s)  # Height

    # Check if the triangle is right-angled
    if s * s == h * h:
        return True
    else:
        return False
```

The function `right_angle_triangle` calculates the height of the triangle based on the sides of the triangle handed to the function. It then checks if the square of the semi-perimeter of the triangle is equal to the square of the height, which is the defining equation of a right-angled triangle.