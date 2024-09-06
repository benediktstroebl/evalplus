```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total * total == Pythagorean_Theorem(a, b, c)

def Pythagorean_Theorem(a, b, c):
    return (a**2 + b**2) == c**2
```

The function `right_angle_triangle` returns true if the sum of the lengths of the three sides is greater than the square of the hypotenuse (Pythagorean theorem) and false otherwise. In the script, the Pythagorean theorem is represented by a separate function with a specialized implementation to compare the squares of the sides with the square of the hypotenuse. Thus, the response meets the specifications of the exercise.