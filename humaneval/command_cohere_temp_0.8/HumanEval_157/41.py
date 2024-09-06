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
The markdown code block above provides a Python script that solves the problem of determining whether the three given sides form a right-angled triangle. The function `right_angle_triangle` takes three parameters `a`, `b`, and `c`, representing the lengths of the triangle's sides. 

The triangle test is used in the function, which provides a quick method to determine if a given triangle is right-angled. The inequality must be met for the triangle to be right-angled: `a^2 + b^2 = c^2`. The function returns `True` if the equation is satisfied, confirming the presence of a right angle. If the equation is not met, the function returns `False`, indicating that the triangle is not right-angled.

This solution is self-contained, easy to use, and follows the problem statement's given convention. It also passes the tests provided alongside the question.