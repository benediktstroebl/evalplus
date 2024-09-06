```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter s of the triangle
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return (s * (s - a) == b * c) or (s * (s - b) == a * c) or (s * (s - c) == a * b)
```

The function utilizes the Pythagorean theorem, which states that in a right triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. 

This approach allows the function to determine whether the given sides can form a right-angled triangle. 

To account for different triangle configurations, the function checks all possible arrangements of the sides provided as arguments.