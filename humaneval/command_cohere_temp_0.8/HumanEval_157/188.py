```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above `right_angle_triangle()` function follows the principle of the Pythagoras theorem, that states whenever the sum of the squares of two sides is equal to the square of the third side, then it is a right-angled triangle. 

Here are some examples demonstrating the usage of the above function:
```python
# Example 1:
print(right_angle_triangle(3, 4, 5))  # Output: True

# Example 2:
print(right_angle_triangle(1, 2, 3))  # Output: False
```

The provided examples successfully validate the accuracy of the function. In the first example, because the square of 5 (25) equals the sum of the squares of 3 and 4 (9 + 16), the function returns True, indicating that the sides form a right-angled triangle. In the second example, since the sum of the squares of 1 and 2 (1 + 4) does not equal the square of 3 (9), the function returns False, indicating that the sides do not form a right-angled triangle.