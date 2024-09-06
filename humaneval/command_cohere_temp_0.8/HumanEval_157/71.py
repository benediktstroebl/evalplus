```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equation of `a^2 + b^2 = c^2` and returns `True` if the triangle formed by the three sides is a right-angled triangle. It returns `False` if it is not a right-angled triangle.