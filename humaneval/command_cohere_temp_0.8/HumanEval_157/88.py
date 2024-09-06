```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or 
    90 degrees.
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

This function checks if the given sides of the triangle form a right-angled triangle according to the Pythagoras theorem, 
which states that in a right triangle, the sum of the squares of the two shorter sides is equal to the square of the longest side. 

Here's the inline explanation of the code:
- The function `right_angle_triangle` takes three parameters `a`, `b`, and `c`, representing the lengths of the three sides of the triangle. 
- The code checks if any of the three possible scenarios of the Pythagoras theorem is true for the given sides, using mutual implication (`or`) to confirm if the triangle is a right-angled triangle.
- If any of the scenarios is satisfied, the function returns `True`, indicating that the given sides form a right-angled triangle. 

The following would be the tests for this function:
```python
# Test case for a right triangle
print(right_angle_triangle(3, 4, 5))  # Expected output: True

# Test case for a non-right triangle
print(right_angle_triangle(1, 2, 3))  # Expected output: False
``` 

This would verify the functionality of the code.