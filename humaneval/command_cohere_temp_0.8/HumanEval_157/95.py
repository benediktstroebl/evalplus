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

The markdown code block above summarizes the solution to the problem statement provided. This solution uses the Pythagorean theorem, a fundamental relationship between the sides of any triangle, to determine if a given set of lengths forms a right triangle. A right triangle possesses a right angle or an angle of 90 degrees. The theorem states that the square of the length of the hypotenuse (c) is equal to the sum of the squares of the lengths of the other two sides (a and b). 

The function returns True if any of the above conditions are met, indicating a right-angled triangle. Otherwise, it returns False, indicating that the sides do not form a right-angle triangle.