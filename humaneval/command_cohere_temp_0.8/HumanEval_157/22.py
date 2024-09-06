```python
def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + a ** 2 == c ** 2:
        return True
    else:
        return False
```

The function checks the conditions of a right-angled triangle as per the prompt's instructions. The first condition checks if a side is equal to another side, and the second condition checks if the square of any two sides of the triangle adds up to the square of the third side, which is a well-known method to check if the sides form a right-angled triangle.