```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
```
The following test cases are built-into the function:
- Test case 1: `right_angle_triangle(3, 4, 5)` returns `True` 
- Test case 2: `right_angle_triangle(1, 2, 3)` returns `False` 
You can further verify the function's correctness by conducting additional tests against other triangle side lengths. 
If you encounter any difficulties or need further assistance, kindly inform us and we shall promptly tend to your needs.