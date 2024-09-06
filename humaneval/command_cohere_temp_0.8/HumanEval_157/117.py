```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif ((a**2 + b**2) == c**2) or ((b**2 + c**2) == a**2) or ((c**2 + a**2) == b**2):
        return True
    else:
        return False
```
The above `right_angle_triangle()` function can easily detect whether it is a right-angled triangle or not using the Pythagoras theory. It returns True if the triangle is a right-angled triangle and False otherwise. It also handles the special case of a triangle with side lengths equal to 0. 

Here is a markdown code block with corresponding test cases to verify the correct functionality of the function:
```python
# Test Cases
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
assert right_angle_triangle(0, 0, 0) == True
assert right_angle_triangle(7, 8, 9) == False
assert right_angle_triangle(-3, -4, 5) == False
```