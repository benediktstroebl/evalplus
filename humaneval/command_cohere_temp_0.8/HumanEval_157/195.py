```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    leg1 = ((b**2) + (c**2) - (a**2))**0.5
    leg2 = ((a**2) + (c**2) - (b**2))**0.5
    
    # Check if the length of the two legs form a right angle
    if leg1**2 + leg2**2 == a**2:
        return True
    else:
        return False
```

The function `right_angle_triangle` determines the lengths of the two legs of the triangle using the Pythagorean theorem. It then calculates the sum of the squares of the lengths of the two legs and compares it to the square of the length of the hypotenuse. If they are equal, it returns True, indicating a right-angled triangle; otherwise, it returns False.

Here is an example of how to use the code:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
``` 

This will return True for the first example because the sides form a right triangle, and False for the second example because it does not form a right triangle.