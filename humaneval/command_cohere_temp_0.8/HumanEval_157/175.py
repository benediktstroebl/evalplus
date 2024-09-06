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

This function checks if the given sides of the triangle form a right-angle using the Pythagoras theorem. 

To do this, it checks if the square of any two sides equals the square of the third side, which will form a right-angle. 

If any of these conditions are met, the function returns True; otherwise, it returns False. 

This function can be used to solve the problem and is self-contained with adequate documentation.