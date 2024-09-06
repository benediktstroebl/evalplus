```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else: 
        return False
```
This function checks if the sum of the squares of two sides of a triangle equals the square of the third side. It returns true if these equations are true for these three sides, and false otherwise.