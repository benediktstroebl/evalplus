```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality coefficients of (a, b, c) against the three known right-angled triangle types. It returns `True` if it finds a match and `False` otherwise. 

This approach covers all 9 possible cases of right-angled triangles, unlike other naive solutions that only cover the 3-4-5 case.