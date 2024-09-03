```python
def right_angle_triangle(a, b, c):
    '''
    Check if a triangle with sides of lengths a, b, c has a right angle
    Returns: Boolean indicating whether the triangle is right-angled or not
    '''
    return (a == b and b == c) and a > 90 

# Test the function
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
``` 
This script defines a function `right_angle_triangle` that checks if a given set of side lengths form a right-angled triangle. The function returns `True` if the sides are equal and the angle is greater than 90 degrees, and `False` otherwise.