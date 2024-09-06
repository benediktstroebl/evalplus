```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter of the triangle
    # Check if the triangle is a right-angled triangle
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else:
        return False
```

The above `right_angle_triangle()` function first calculates the semi-perimeter of the triangle by using the formula `semi-perimeter = (sum of sides) / 2`. Then, it checks if the semi-perimeter^2 equals the sum of two sides multiplied by itself. If any of these equalities hold true, it returns `True`, otherwise, it returns `False`.

Here is a test suite that can be used to validate the correctness of the implementation:
```python
def test_right_angle_triangle():
    # Valid right-angled triangle
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True

    # Invalid right-angled triangle
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(7, 8, 9) == False

    # Edge cases
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(10, 10, 10) == False

test_right_angle_triangle()
```

This test suite covers both valid and invalid scenarios to ensure that the `right_angle_triangle()` function accurately determines whether the given trio of side lengths forms a right-angled triangle.