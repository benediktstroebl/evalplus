```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equivalence of all three combinations of the input sides `a`, `b`, and `c`. If any of these equations are true, then this function returns `True` as the triangle is a right-angled triangle; otherwise, it returns `False`. 

This solution should help you pass any basic test cases, but it's worth noting that this approach can be improved for edge cases (such as where one or more sides might be zero). 

Let me know if you'd like to discuss optimizations or further details on the logic behind this!