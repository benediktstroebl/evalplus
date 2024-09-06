```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of a right triangle
    s = (a**2 + b**2 + c**2)**0.5
    p = (a**2 + c**2 - b**2)**0.5

    # Determine if the triangle is right angled
    if s**2 + p**2 == c**2:
        return True
    else:
        return False
```

This function follows the Euclidean definition of a right triangle, directly from the Pythagorean theorem. It compares the sum of the squares of the two legs (`s` and `p`) to the square of the hypotenuse (`c`).

It returns True if the triangle is right-angled, and False otherwise. You can easily adapt this function to suit the unit tests you mentioned.