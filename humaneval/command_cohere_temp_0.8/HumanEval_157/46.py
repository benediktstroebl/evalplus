```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    if (a == 0 or b == 0 or c == 0) and (a + b > c) and (a + c > b) and (b + c > a):
        return True
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return True
    return False
```

This Python script defines a function called `right_angle_triangle` that takes three arguments: `a`, `b`, and `c`, which represent the lengths of the three sides of a triangle. 

The function first handles the edge case of a triangle with zero length sides:
1. It returns `True` if all three sides are zero, excluding the case of zero-length sides.
2. It returns `True` if one side is zero, but only if the sum of the two non-zero sides is greater than the longest side, satisfying the Pythagoras theorem.

Then it performs the Pythagoras rule checks for right angle triangles:
1. It returns `True` if the square of any two sides is equal to the square of the third side, which is a definition of a right-angled triangle.

Here's an example of how to use the function:
```python
print(right_angle_triangle(3, 4, 5))  # Outputs: True
print(right_angle_triangle(1, 2, 3))  # Outputs: False
```

This script ensures that the function `right_angle_triangle` accurately determines whether the given sides form a right-angled triangle or not.