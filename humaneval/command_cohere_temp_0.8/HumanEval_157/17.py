```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    # Check if the triangle is a right-angled triangle
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else: 
        return False
```

The above `right_angle_triangle()` function follows the definition of a right-angled triangle mentioned in the problem statement. The function calculates the semi-perimeter of the sides of the triangle and then checks if the above three conditions are satisfied. If any one of these conditions is true, it returns `True`, otherwise `False`.

This approach is computationally efficient with a time complexity of O(1) and is compatible with the design of the problem statement.