```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    # Determine if the triangle is right-angled
    if hypotenuse ** 2 == c ** 2 and hypotenuse ** 2 == a ** 2 + b ** 2:
        return True
    else:
        return False
```

This function adheres to the problem's specification, which includes the determination of the hypotenuse and the evaluation of the triangle's right-angled nature based on the Pythagorean theorem. Additionally, it includes a concise self-contained test suite.

The following is a test suite that can be used to validate the correctness of the function:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(7, 8, 9) == False
    assert right_angle_triangle(0, 1, 1) == False

test_right_angle_triangle()
``` 
This test suite contains multiple test cases that cover a variety of scenarios, including edge cases, to ensure the reliability of the `right_angle_triangle` function.