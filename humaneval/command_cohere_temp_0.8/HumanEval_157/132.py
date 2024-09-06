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

To do this, it checks if the sum of the squares of any two sides is equal to the square of the remaining side. If any of 
these conditions are met, it returns True; otherwise, it returns False. 

This logic follows the Pythagoras theorem which states that the square of the hypotenuse (the side opposite the right 
angle) is equal to the sum of the squares of the other two sides. 

This approach does not require any imported libraries. 

Thus, the function is self-contained and can be executed independently.