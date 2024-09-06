```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above `right_angle_triangle()` function implements the logic of a right-angled triangle. 

To correctly check if the triangle is a right-angled triangle, the Pythagoras theorem is used, that is, a right-angled triangle has one right angle, and the areas of the squares on the sides of the triangle add up to the fourth power of the hypotenuse.

The code block passes the given tests and outputs the correct values.