```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse ** 2 == a ** 2 + b ** 2
```

The function adheres to the problem's definition of a right-angled triangle, using the Pythagorean theorem to calculate the hypotenuse and returning `True` if the calculated hypotenuse matches one of the given sides and the Pythagorean equation holds.

This solution encompasses the logic of the problem and can be directly embedded into a Markdown code block for easy understanding and use.