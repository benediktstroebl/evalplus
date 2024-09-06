```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle with the greatest angle
    s = (a + b + c) / 2  # the semi-perimeter of the triangle
    r = sqrt(s * (s - a) * (s - b) * (s - c))  # the radius of the circle inscripted the triangle

    return r == abs(a - b) or r == abs(a - c) or r == abs(b - c)
```

The function calculates the semi-perimeter and the radius of the circle inscribed in the triangle. It then compares the inscribed radius with the side lengths to determine if the triangle is right-angled.

To achieve a markdown code block, you can copy and paste this code into a Markdown file with a single line of code per line of code in the code block.