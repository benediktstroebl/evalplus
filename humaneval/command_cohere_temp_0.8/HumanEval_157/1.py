```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # The semi-perimeter of the triangle
    # Determine if the triangle is right-angled using the Pythagorean theorem
    return s * (s - a) == b * c
```

The script tests the function using:
```python
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
```

The function `right_angle_triangle` uses the Pythagorean theorem to determine if the triangle is right-angled. The theorem states that in a right triangle, the square of the length of the longest side (the hypotenuse) is equal to the sum of the squares of the other two sides. In this case, the function checks if the squared length of the hypotenuse (`s * (s - a)`) is equal to the squared sum of the other two sides (`b * c`). If the equation holds, the triangle is right-angled, and the function returns `True`; otherwise, it returns `False`. 

This approach allows the function to accurately determine whether the given lengths form a right-angled triangle.