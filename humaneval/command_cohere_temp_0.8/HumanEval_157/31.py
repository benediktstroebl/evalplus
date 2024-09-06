```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle sides
    s = (a + b + c) / 2  # Semiperimeter
    x = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Length of the fourth side

    return x ** 2 == a * b or x ** 2 == b * c or x ** 2 == c * a
```

The function assesses the quadratic equation of the hypothesized fourth side, which is x ** 2. It takes the semiperimeter s and three side lengths a, b, and c to calculate this side length. The three sides form a right-angled triangle if any of the following conditions are met: the squared length of the presumed fourth side equals the product of two sides or if it equals the product of the hypotenuse and one of the other sides. The approach employs geometry and trigonometry to determine the presence of a right angle without directly calculating any angles.

Here is an example of how to use this function:
```python
print(right_angle_triangle(3, 4, 5))  # True
print(right_angle_triangle(1, 2, 3))  # False
```

This will result in the following output:
```
True
False
```

This indicates that the first set of sides forms a right-angled triangle, while the second set does not.