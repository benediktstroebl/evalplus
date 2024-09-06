```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints required to identify a right-angled triangle. 

For a right triangle with legs of length 'a' and 'b' and hypotenuse 'c', one of the following must be true:

- a^2 + b^2 = c^2
- a^2 + c^2 = b^2
- b^2 + c^2 = a^2

If any of these are true, then the triangle is a right triangle. If none of these are true, then it is not a right triangle. 

This logic aligns with the request's directive to check whether the sides form a right-angled triangle based on their lengths. 

This script can be used as a simple function to determine whether a set of three sides form a right-angle triangle. 

If the equality condition is met, it returns True; otherwise, it returns False.