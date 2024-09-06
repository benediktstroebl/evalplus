```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides. 

This theorem is the key to determine whether the triangle is a right-angled triangle or not. If any of the three possible combinations of the sides' lengths result in the Pythagorean equation, the function returns True, and else it returns False. 

To better illustrate how the function works, let's cite the examples from the problem statement:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This script should correctly answer the question and pass the tests corresponding to the given problem statement.  It's best to include this code within a testing framework, such as unittest, to ensure robustness and cover all edge cases.  If you're interested in more details on unit testing in Python, please let me know.