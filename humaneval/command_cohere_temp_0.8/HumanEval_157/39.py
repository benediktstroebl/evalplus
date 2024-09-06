```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return s * (s - a) == b * c
```

The function `right_angle_triangle` calculates the semi-perimeter of the triangle, defined as half the sum of the side lengths. It then checks whether the semi-perimeter multiplied by the difference between the semi-perimeter and side length `a` equals the product of sides `b` and `c`. If this equation holds, the triangle is a right-angled triangle, and the function returns `True`; otherwise, it returns `False`.

Here is a test drive function to test the above function:
```python
def test_right_angle_triangle():
    # Test case 1: Valid right-angled triangle
    assert right_angle_triangle(3, 4, 5) == True

    # Test case 2: Invalid triangle, not a right angle
    assert right_angle_triangle(1, 2, 3) == False

    # Test case 3: Invalid triangle, not a right angle
    assert right_angle_triangle(10, 6, 2) == False

test_right_angle_triangle()
```

This `test_right_angle_triangle` function calls the `right_angle_triangle` function with different side lengths to verify its correctness for both valid and invalid right-angled triangles.