```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The function checks for the zeroes length, where all sides are zero and there is a right angle. Then it checks for the hypotenuse using the Pythagorean theorem, where b**2 + c**2 == a**2. 

This approach ensures that the function correctly determines whether the given lengths form a right-angled triangle.