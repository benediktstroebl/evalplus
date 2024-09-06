```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Determine if the triangle is right-angled
    if hypotenuse == c or hypotenuse ** 2 == c ** 2 + b ** 2 or hypotenuse ** 2 == a ** 2 + c ** 2:
        return True
    else:
        return False
```

The function `right_angle_triangle` swiftly computes the length of the hypotenuse and checks whether the triangle represents a right-angled triangle. It returns True if any of the conditions are met, and False otherwise, which aligns with the specified conditions for a right-angled triangle. Feel free to utilize this function to efficiently solve problems related to right-angled triangles.  If you want more explanations on any of the steps, just let me know.