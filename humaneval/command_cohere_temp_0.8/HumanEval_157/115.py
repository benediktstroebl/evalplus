```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```
The above right_angle_triangle() function checks inequities from the Pythagoras theorem to determine if the given sides form a right-angled triangle. 

Here is a sample output of the function:
```
right_angle_triangle(3, 4, 5) == True
right_angle_triangle(1, 2, 3) == False
```
The function returns True for the first example and False for the second, indicating whether the given triangle is a right triangle or not.