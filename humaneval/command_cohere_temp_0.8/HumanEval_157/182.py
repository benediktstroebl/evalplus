```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or
    90 degrees.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks if the given sides of the triangle form a right-angled triangle. It does so by checking if the sum of the squares of two sides is equal to the square of the remaining side, which is a well-known criterion for a right-angled triangle. The function returns True if the triangle is right-angled and False otherwise. And the function is fully self-contained and easily executable within a markdown cell.