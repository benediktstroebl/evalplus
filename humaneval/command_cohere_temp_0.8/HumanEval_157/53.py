```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of the triangle using the Pythagorean theorem, which states that the sum of the squares of the two shorter sides is equal to the square of the longest side. 

Here's an example of how to use the function:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This will return `True` for the first example because the lengths of the sides make a right-angled triangle, while the second will return `False` since the sides do not form a right-angled triangle.