```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = sqrt(s*(s-a)*(s-b)*(s-c))  # Height

    # Check if the triangle is right-angled using the Pythagorean theorem
    return h == b or h == a or h == c
```

The function leverages the Pythagorean theorem to determine whether the triangle is right-angled. 

To do this, it first calculates the semi-perimeter s of the triangle, defined as `s = (a + b + c) / 2`, where a, b, and c are the lengths of the three sides.

Next, it calculates the height h of the triangle using the formula `h = sqrt(s * (s - a) * (s - b) * (s - c))`. This height h is the hypotenuse of a right-angled triangle with sides of length s, a, and b.

Finally, the function returns True if the height h is equal to any of the sides a, b, or c. If any of these conditions are true, it signifies that the triangle is right-angled, as the height of a right-angled triangle will always be equal to one of its sides.

This approach allows the function to accurately determine whether the given lengths form a right-angled triangle, without requiring additional calculations based on the supplied input. 

It is important to ensure that the function is tested adequately to validate its correctness across various edge cases.