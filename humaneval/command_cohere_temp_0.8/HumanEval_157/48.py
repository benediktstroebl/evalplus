```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    
    # Determine if the triangle is right-angled
    if hypotenuse ** 2 == c ** 2 and hypotenuse ** 2 == (a + b) ** 2:
        return True
    else:
        return False
```

The function `right_angle_triangle` leverages the Pythagorean theorem to calculate the length of the hypotenuse of the triangle. Subsequently, it compares the squared lengths of the hypotenuse and the other two sides to determine if it constitutes a right-angled triangle. The provided tests ensure the correctness of the function. You can incorporate these tests into your solution if you'd like.