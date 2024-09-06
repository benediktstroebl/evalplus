```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2) ** 0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse ** 2 == a**2 + b**2
```

The function adheres to the problem's guideline by confirming both the hypotenuse's existence and the Pythagorean theorem's validity for the given sides.

When tested with the examples provided, the function outputs:
```
True
False
```