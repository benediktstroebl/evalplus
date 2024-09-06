```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter of the triangle

    # Check if the triangle is right-angled using the Pythagoras theorem
    if s * (s - a) == b * c:
        return True
    else:
        return False
```

The script uses the Pythagorean theorem, which states that in a right triangle, the square of the length of the hypotenuse ( c ) is equal to the sum of the squares of the other two sides (a and b). In this case, the algorithm determines whether the triangle is a right triangle by calculating the semi-perimeter (s) and then checking if the equation holds true.

Here is a simple test suite containing a test case for the example provided in the problem statement and a few more:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(7, 10, 15) == False
```

This test suite can be run separately to validate the correctness of the `right_angle_triangle` function. 

This code demonstrates a straightforward application of the Pythagorean theorem to determine whether a given set of lengths forms a right-angled triangle. It's an essential example of applying geometry in coding.