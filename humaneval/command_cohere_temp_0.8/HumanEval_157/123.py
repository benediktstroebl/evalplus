```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

This function checks if the given sides form a right-angled triangle according to the Pythagoras theorem, 
which states that in a right triangle, the sum of the squares of the two smaller sides is equal to the square of the hypotenuse. 

Additionally, the function's correctness can be verified by passing relevant cases like:
```python
 tester = unittest.TestCase()
 tester.assertEqual(right_angle_triangle(3, 4, 5), True)
 tester.assertEqual(right_angle_triangle(1, 2, 3), False)
```

Note: ensure you have Python modules `unittest` and `unittest. TestCase()` installed and imported to run the test cases. 
This can be done with `from unittest import TestCase` and `unittest.main()'` for executing the test suite.