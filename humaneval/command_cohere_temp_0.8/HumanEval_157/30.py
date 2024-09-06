```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the sum of the squares of two sides of the triangle against the square of the third side, pursuant to the Pythagoras theorem. If the equation holds, the triangle is a right-angled triangle, if not, it returns False. 

To ensure that the function handles the decimal number cases, one should consider converting the inputs to floats before doing the comparison, like so: 

```python
def right_angle_triangle(a, b, c):
    if float(a**2 + b**2) == float(c**2) or float(a**2 + c**2) == float(b**2) or float(b**2 + c**2) == float(a**2):
        return True
    else: 
        return False
``` 

This modification allows the function to correctly identify right-angled triangles with side lengths containing decimals.