```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or
    90 degrees.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else:
        return False
```

This function checks if the sum of the squares of any two sides is equal to the square of the remaining side, which is a determinant of a right-angled triangle. 

Also, you can improve the performance of this function by introducing a bounding condition that checks if the triangle's sides are relatively small before performing the square root operation. This can be done by checking if the absolute value of the difference between any two sides is less than or equal to the square root of the smallest side, as follows:
```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle.
    Return True if the three sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle or
    90 degrees.
    """
    min_side = min(a, b, c)
    if abs(a - b) <= min_side ** 0.5 or abs(b - c) <= min_side ** 0.5 or abs(c - a) <= min_side ** 0.5:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        else:
            return False
    else:
        return False
```
This updated version provides a more efficient solution to the right-angle triangle problem. You can test it using the following example:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```

This improved version ensures that the function performs fewer operations by only proceeding with the square root comparison if the sides are within a certain range.