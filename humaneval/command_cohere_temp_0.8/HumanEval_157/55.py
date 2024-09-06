```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    
    # Check if the triangle is right-angled
    if hypotenuse == c or hypotenuse ** 2 == c ** 2 + b ** 2 or hypotenuse ** 2 == a ** 2 + c ** 2:
        return True
    else:
        return False
```

The function `right_angle_triangle` calculates the length of the hypotenuse and then checks if the given lengths form a right-angled triangle according to three conditions: hypotenuse equals the longest side, Pythagoras' theorem, or the sum of the squares of the two shorter sides. All three conditions check for the same mathematical relationship, ensuring the 90-degree angle.

This approach covers all the scenarios mentioned in the problem statement and is generally more efficient than a brute-force approach that checks all three angles. It also has a more efficient runtime of O(1) since it doesn't involve manipulating trigonometric functions or iterating through unnecessary calculations.