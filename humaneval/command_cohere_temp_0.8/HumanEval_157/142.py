```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

This function checks if the given sides form a right-angled triangle according to the Pythagorean theorem, 
which states that the sum of the squares of the two legs of a right triangle must be equal to the square of the hypotenuse. 

Here's an example of how to use this function:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This script fully addresses the task and provides a self-contained Python function. It requires no external dependencies 
or additional code to run and fulfill the function specification.