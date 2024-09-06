```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return (s * (s - a) == b ** 2) or (s * (s - b) == a ** 2) or (s * (s - c) == c ** 2)
```

The function utilizes the Pythagorean theorem, which states that in a right triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.

To determine if the triangle is right-angled, it calculates the semi-perimeter s and checks if any of the following conditions are met:
1. s * (s - a) == b^2 : The square of the difference between the semi-perimeter and side a is equal to the square of side b.
2. s * (s - b) == a^2 : The square of the difference between the semi-perimeter and side b is equal to the square of side a.
3. s * (s - c) == c^2 : The square of the difference between the semi-perimeter and side c is equal to the square of side c.

If any of these conditions hold true, it means that the triangle is right-angled, and the function returns True; otherwise, it returns False.

This approach allows the function to efficiently determine whether the given lengths of the three sides form a right-angled triangle without iterating through all possible combinations of sides.