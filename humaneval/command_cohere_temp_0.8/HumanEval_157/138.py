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

This function checks if the given sides of the triangle form a right-angled triangle according to the Pythagorean theorem,  `a^2 + b^2 = c^2`. It returns `True` if the sides form a right-angled triangle and `False` otherwise. This method is highly efficient, and its runtime is constant linear time `O(1)`. 

This function can be tested with a simple unit test:
```python
>>> test = [
...     ([3, 4, 5], True),
...     ([1, 2, 3], False),
...     ([7, 8, 9], False),
...     ([5, 12, 13], True),
... ]
>>> for side, result in test:
...     assert (right_angle_triangle(*side) == result)
```

This unit test checks the correctness of the `right_angle_triangle` function by passing it test cases and comparing the output with the expected `True` or `False` value.