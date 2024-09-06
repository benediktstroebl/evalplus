```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of a triangle using the Pythagorean theorem, threom conveys a right-angled triangle. This is done by checking if the square of the first two sides is equal to the square of the third side, which is the hypotenuse. 

To ensure that the function adheres to the Pythagorean theorem, the inputs are assumed to be integers, as this is a common Pythagorean theorem implementation.