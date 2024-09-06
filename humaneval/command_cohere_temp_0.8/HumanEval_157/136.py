```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

The script defines a function 'right_angle_triangle' that takes three parameters 'a', 'b', and 'c', representing the lengths of the three sides of a triangle. It returns 'True' if the sides form a right-angled triangle, characterized by having one 90-degree angle, and 'False' otherwise. 

The function checks this condition in a straightforward manner, checking if any of the symmetrical equations ((a**2 + b**2 = c**2), ((a**2 + c**2 = b**2), or ((b**2 + c**2 = a**2)) hold true. If any of these conditions are met, it returns 'True', and if none do, it returns 'False'. 

This simple function provides a quick way to determine whether a set of numbers represents the sides of a right-angled triangle, making it useful for various applications involving geometry or trigonometry. 

To ensure the function's correctness, it is recommended to verify it with multiple test cases, like the ones provided in the problem statement. Doing so will help ensure that the function behaves as expected and aligns with the problem's requirements, delivering a reliable solution.