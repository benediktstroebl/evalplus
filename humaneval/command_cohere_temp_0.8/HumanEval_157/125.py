```python
def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + a ** 2 == c ** 2:
        return True
    else:
        return False
```

The function checks through three conditions:
1. If any of the sides are equal to each other, it returns true.
2. If the sum of the squares of two sides is equal to the square of the other side, it returns true.
3. If none of the above conditions are met, it returns false. 

The function checks for these conditions to determine if the three given sides form a right-angled triangle. 

To ensure this function's effectiveness, the input values must be integers or have the `sqrt()` function available in Python. Floating point numbers or irrational numbers like π may lead to inaccurate results. 

Overall, the code provides an effective solution by checking the conditions necessary to determine a right-angled triangle. 

Note: ensure the length of the sides is positive to avoid infinite loops when calculating the square root. Consider using absolute value or handle negative values beforehand to ensure robustness.