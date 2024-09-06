```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints required to identify a right-angled triangle. It returns True if any of these conditions are met, and False otherwise. These conditions are based on the theory that the sum of the squares of the two shorter sides of a right-angled triangle must equal the square of the longest side, which is known as the hypotenuse.