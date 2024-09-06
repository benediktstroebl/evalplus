```python
def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return True
    else:
        return False
```

This function checks the triangle inequality first. If the given sides do not violate the inequality, it then checks if any of the Pythagorean triple equations are valid. The function returns 'True' if the triangle is right-angled, and 'False' otherwise. 

To check the correctness of the solution, feel free to plug in different triplets of numbers for the function and see if the output corresponds to the hypothesized right-angled triangles from the problem statement. 

Let me know if you'd like me to make any adjustments or add any additional details!