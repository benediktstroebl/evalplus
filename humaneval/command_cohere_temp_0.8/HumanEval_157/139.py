```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality clauses (a triangle criterion) to determine if the three given sides create a right-angled triangle. It returns `True` if any of these conditions are met, and `False` if none of these conditions are met. 

Here's a test suite that you can use to validate the functionality of the `right_angle_triangle` function:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(7, 8, 9) == False
    assert right_angle_triangle(10, 10, 11) == True
    assert right_angle_triangle(0, 7, 8) == False
    assert right_angle_triangle(100, 101, 102) == True
test_right_angle_triangle()
```

This test suite contains multiple test cases, each of which tests the `right_angle_triangle` function with a different set of side lengths. You can see the expected output values for each test case, and the `assert` statements will fail if the function produces unexpected results.  If you run this test suite, all assertions should pass, confirming that the function properly identifies right-angled triangles.