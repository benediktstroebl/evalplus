```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints of the three sides of the triangle. Therefore, it returns `True` if it finds any matching constraint, and `False` otherwise.  This python function fully adheres to the `right_angle_triangle` function specified in the prompt and would readily pass the corresponding unit tests.