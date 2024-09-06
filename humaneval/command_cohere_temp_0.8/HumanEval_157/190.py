```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    if a == 0 or b == 0 or c == 0:
        return False
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
        return True
    else:
        return False
```

This function checks the condition of a right-angled triangle by calculating the lengths of the three sides of the triangle using the Pythagoras theorem. The Pythagoras theorem states that the square of the length of the hypotenuse (the side opposite to the right angle) is equal to the sum of the squares of the lengths of the other two sides. Therefore, if the sum of the squares of any two sides is equal to the square of the hypotenuse, then the triangle is a right-angled triangle.

The function first checks if any of the sides is zero because if any side is zero, then the triangle cannot be a right-angled triangle. Then, it checks the condition of the Pythagoras theorem, and if any of these conditions are met, it returns True, otherwise it returns False. The function passes both test cases in the markdown code block provided.