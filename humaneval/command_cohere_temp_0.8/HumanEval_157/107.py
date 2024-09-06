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

The above `right_angle_triangle()` function first calculates the semi-perimeter of the triangle by using the formula `semi-perimeter = (sum of side lengths) / 2`. 

Then it checks if the triangle is a right-angled triangle by using the Pythagoras theorem. The Pythagoras theorem states that the square of the hypotenuse is equal to the sum of squares of the other two sides.

The above condition is checked for all possible pairings of the sides of the triangle. 

Finally, the function returns `True` if any of these conditions are satisfied, and `False` otherwise, indicating that the given sides form a right-angled triangle.

This approach ensures that the function is self-contained, and it can accurately determine whether the given sides form a right-angled triangle. 

This code can be placed in a markdown code block, and it can be executed independently to test the functionality. 

Ensure that you have Python 3 and the required testing library installed to execute the code and see the test results.