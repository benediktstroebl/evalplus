```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equivalence of all combinations of the three sides to determine if it forms a right-angled triangle. 

For example, the given example tests would yield: 
 ```python
right_angle_triangle(3, 4, 5) == True
right_angle_triangle(1, 2, 3) == False
```