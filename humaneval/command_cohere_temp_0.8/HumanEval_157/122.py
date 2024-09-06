```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    h = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Height

    # Verify that the triangle is right-angled
    return h == b or h == c or h == a
```

This approach involves using the Pythagorean theorem to first calculate the height `h` of the triangle when given the sides `a`, `b`, and `c`. The function then compares the calculated height against the side lengths to determine if the triangle is right-angled. This is a well-known approach to detecting right-angled triangles among three given sides. 

To better understand the correctness of the approach, let's break down the Python script:
1. The semi-perimeter `s` of the triangle is calculated using the formula for the circumradius of a triangle (`s = (a + b + c) / 2`). The circumradius is the radius of the circle inscribing the triangle).
2. Using the semi-perimeter and the formula for the height of a right-angled triangle (`h = (s * (s - a) * (s - b) * (s - c)) ** 0.5`), the function calculates the height `h` of the triangle. This height corresponds to the side that faces the right angle in the triangle.
3. The function returns `True` if the height matches any of the given sides of the triangle (`h == b` or `h == c` or `h == a`). This is because the height corresponds to one of the sides in a right-angled triangle. 

This approach works for any valid input of side lengths, as long as the input represents a valid order of sides for a triangle (i.e., the sum of side lengths is greater than 0 and less than infinite). 

Note, the approach assumes that the input is valid and that the sides provided form a triangle. Additional validation or error handling is left to the user to implement, if necessary.