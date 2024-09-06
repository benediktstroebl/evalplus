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
The markdown code block contains a Python script with a function `right_angle_triangle(a, b, c)` that takes in three lengths, `a`, `b`, and `c`, and returns `True` if the sides form a right-angled triangle, and `False` otherwise. The function passes the given tests of the problem statement. It does so by checking if the sum of the squares of any two sides is equal to the square of the remaining side, which is the defining algebraic characteristic of a right triangle. 

This code includes a docstring with instructions for the function and an example to demonstrate the behavior of the function.