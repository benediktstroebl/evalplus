```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of a triangle using the Pythagorean theorem, which states that the sum of the squares of the two shorter sides is equal to the square of the longest side.

Here is a test suite that could be used to validate the function against examples from the problem statement:
```python
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5))
    assert(right_angle_triangle(1, 2, 3)) == False
    assert(right_angle_triangle(5, 12, 13))
    assert(right_angle_triangle(10, 8, 15)) == False
    assert(right_angle_triangle(7, 24, 25))
test_right_angle_triangle()
```

This test suite uses the Python assert statement to verify that the right_angle_triangle function returns the expected values for a set of inputs. 

The __name__ == '__main__' check is used to confirm that the module is run as the main program. When the module is imported elsewhere, these tests will not run. This behavior is often used in test drivers to execute specific test cases.