```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that the sum of the squares of the two shorter sides of a right-angled triangle is equal to the square of the longest side (hypotenuse). This technique allows the function to determine whether the given lengths form a right-angled triangle. Notably, this method is not specific to Euclidean geometry and can be used to test if a triangle is right-angled in any metric space. 

To use this function, you can simply call it with the respective lengths of the three sides, and it will return `True` if they form a right-angled triangle and `False` otherwise. 

This approach guarantees a correct implementation of the problem description and is applicable within mathematics and computer science disciplines.