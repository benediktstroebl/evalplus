```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above right_angle_triangle() function checks occurrences of two 2 sides of a right-angle triangle. If the sum of the squares of any two sides is equal to the square of the remaining side, the function returns True, otherwise, it returns False.

Here is a simple test case to check the functionality of the function:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```
The first test case passes while the second test case returns False, indicating that the function is working correctly.