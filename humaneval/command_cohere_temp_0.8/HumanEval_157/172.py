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

The function `right_angle_triangle` calculates the semi-perimeter of the triangle by summing the sides and dividing by 2. It then checks if the triangle is a right-angled triangle by using the Pythagorean identity. 

To verify the accuracy of the function, you can use the following tests:
```python
test_cases = [
    (3, 4, 5, True),
    (1, 2, 3, False),
    (5, 12, 13, True),
    (2, 4, 6, False)
]

for a, b, c, expected in test_cases:
    assert right_angle_triangle(a, b, c) == expected
```

This block of code creates a list of test cases for the function, where each test case is a set of input values (the lengths of the three sides of the triangle) and the expected output (whether the triangle is a right-angled triangle). The `right_angle_triangle` function is then called for each test case, and the actual output is compared to the expected output using the `assert` statement. 

If all assertions pass, it indicates that the function `right_angle_triangle` is correct and successfully identifies right-angled triangles based on the given lengths of the sides.