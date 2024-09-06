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
The above right_angle_triangle() function checks whether the given sets of sides form a right-angled triangle. The function returns True if the sum of square of two sides is equal to the square of the third side. We have used the Pythagoras theory here to determine the right-angled triangle. The function returns False if the sum of square of two sides is not equal to the square of the third side. 

Here is a simple test case:
```python
print(right_angle_triangle(3, 4, 5))
```
Output:
True

And here is a false test case:
```python
print(right_angle_triangle(1, 2, 3))
```
Output: 
False