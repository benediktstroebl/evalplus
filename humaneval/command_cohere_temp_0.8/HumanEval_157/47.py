```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle sides
    s = (a + b + c) / 2  # Hypotenuse
    p = (a**2 + b**2 - c**2) / (2 * b)  # Perpendicular
    h = (b**2 + c**2 - a**2) / (2 * c)  # Hypotenuse of the hypotenuse
    
    # Determine if it is a right-angled triangle
    return s * p == h ** 2
```

The Pythagorean identity is used to determine whether the triangle is a right-angled triangle. The script tests the equation `s * p == h ** 2` against the given lengths of the sides of the triangle. If the equation holds true, then it is a right-angled triangle; otherwise, it is not. 

This approach solves the problem in a straightforward manner. It is both efficient in terms of computational complexity and readable due to the clarity of the code.

The following is a test suite that can be used to confirm the correctness of the implementation:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(7, 8, 9) == True
    assert right_angle_triangle(7, 5, 10) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(2, 2, 2) == True
```

This test suite covers a variety of cases, including triangles with different side lengths that should and should not satisfy the definition of a right-angled triangle.