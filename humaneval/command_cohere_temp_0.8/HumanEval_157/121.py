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

The markdown code block above provides a Python script that solves the problem of determining whether the three given sides of a triangle form a right-angled triangle, using the Pythagorean theorem. 

The function returns True if the sum of squares of any two sides equals the square of the third side, which is a characteristic of right-angled triangles. Otherwise, it returns False. 

This approach does not require additional imports and is self-contained within the function.  It provides clear documentation of the function for easy comprehension.  It is also versatile and accommodates various triangle side inputs as exemplified in the provided examples in the docstring.  This helps in dispelling any confusion when diagnostically approaching this issue.  This is a helpful tool in the toolbox of developers when faced with real-world trigonometry problems.