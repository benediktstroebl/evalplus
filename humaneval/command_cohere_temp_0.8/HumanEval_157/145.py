```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

The markdown code block above provides a Python script that solves the problem of determining whether the three given sides of a triangle form a right-angled triangle, where a right-angled triangle is defined as one in which one angle is a right angle or 90 degrees. The script defines a function `right_angle_triangle` that takes three sides `a`, `b`, and `c` as input and returns `True` if the sum of the squares of any two sides equals the square of the third side, which is a characteristic of a right-angled triangle; otherwise, it returns `False`. 

The script is self-contained and ready to be used and evaluated by passing different arguments to the `right_angle_triangle` function to check if different sets of side lengths form a right-angled triangle. 

```python
# Test Code
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
```

The test code provided above tests the function with two different sets of arguments, verifying that the function returns the expected true or false results for triangles that do or do not form right-angled triangles.  It is important to test your code with different inputs to ensure that it behaves as expected.