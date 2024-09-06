```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that the sum of the squares of the two shorter sides of a right-angled triangle is equal to the square of the longest side (the hypotenuse). 

To determine whether the triangle is right-angled, the function compares the sum of the squares of a and b to the square of c, or alternatively, compares the sum of the squares of a and c to the square of b, or the sum of the squares of b and c to the square of a. 

If any of these conditions are met, it returns True, and it returns False otherwise. 

This approach allows the function to accurately determine whether the given lengths of a, b, and c form a right-angled triangle.