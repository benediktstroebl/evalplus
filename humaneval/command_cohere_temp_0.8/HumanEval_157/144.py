```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints of the triangle. It returns True if any of the three possible pairings of sides yield a 2a + 2b = c right triangle and False otherwise. It is based on Pythagoras' theorem which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.