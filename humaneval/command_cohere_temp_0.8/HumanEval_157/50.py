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
The above right_angle_triangle() function checks, by using the Pythagoras equation, the three sides of the triangle against several well-known triangle types. It returns 'True' if it is a right-angled triangle, and 'False' otherwise. 

To ensure this function works effectively, it is essential to ensure that the Pythagoras equation (a**2 + b**2 = c**2) is accurate, proper unit testing, and well-documented to assist users in understanding the problem and providing examples. 

This approach ensures that the function is entirely self-contained and does not rely on external variables or assumptions. It also adheres to Python's elegant and simple style while delivering a robust and accurate solution to the problem statement.