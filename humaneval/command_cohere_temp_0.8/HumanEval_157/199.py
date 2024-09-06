```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or
    90 degrees.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks if the sum of the squares of any two sides is equal to the square of the remaining side, which is a defining characteristic of a right triangle. It returns True if this condition is met, and False otherwise. 

To test this function, you can use a simple unit test, like so:
```python
# This is the test for the right_angle_triangle function
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5)) == True
```

This tests the function on a known valid triangle and guarantees that it passes. You can then run this test case as follows:
```python
test_right_angle_triangle()
``` 

This will ensure that the function operates correctly.