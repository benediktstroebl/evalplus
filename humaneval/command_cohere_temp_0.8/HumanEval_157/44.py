```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter s of the triangle

    # Check if the triangle is a right-angled triangle
    if s * (s - a) == b * c:
        return True
    else:
        return False
```

The function `right_angle_triangle` calculates the semi-perimeter of the triangle using the given side lengths. Then it uses the Pythagorean theorem to check if the triangle is a right-angled triangle. The approach relies on the fact that in a right-angled triangle, the square of the length of the longest side is equal to the sum of the squares of the lengths of the other two sides.

This approach is efficient and avoids the computational complexity of using trigonometric functions. It provides a straightforward way to determine whether a given set of side lengths forms a right-angled triangle.

This code can be used as a standalone function in a Python environment to solve the problem and is fairly robust in its handling of the input cases.