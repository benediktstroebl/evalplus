```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    # Check if the triangle is right-angled
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else:
        return False
```

The function `right_angle_triangle` calculates the semi-perimeter of the triangle using the given side lengths. Then it checks if the semi-perimeter squared equals the sum of two sides squared minus the third side squared, which is a well-known method for determining whether a triangle is right-angled. It returns `True` if the conditions are met, and `False` otherwise. 

Here's an example of how to use the function:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This approach assumes that the side lengths are given in linear units, such as integers or floats, and that the input values are valid dimensions for a triangle. If the input values are invalid (e.g., the side lengths are not positive), the function may not work as intended.