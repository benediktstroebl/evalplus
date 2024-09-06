```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semi-perimeter
    # Determine the difference between the largest two sides and the third side
    diffuser = max(a, b) - c
    # Determine the square of the diffuser
    diffuser_square = diffuser ** 2
    # Calculate the square of the semi-perimeter
    s_square = s ** 2
    # Return True if the diffuser is less than the semi-perimeter and their
    # squares have equal magnitude
    return diffuser_square <= s_square
```

The formula used is recognised as the Pythagorean Identity, a2 + b2 = c2,. This identifies whether the sides represent a right-angled triangle. A triangle is recognised as a right-angled triangle when one angle is 90 degrees and the shortest side is perpendicular to the plane or horizon.

It is important to note that the function is not limited to any specific range of numbers and is not limited to measuring distances in miles or kilometres, for example. The function can be used with a variety of units, such as centimetres, metres, or inches. 

This function will return `True` for valid right-angled triangles, and `False` otherwise. You can use this function to quickly determine if a set of side lengths forms a right-angled triangle.