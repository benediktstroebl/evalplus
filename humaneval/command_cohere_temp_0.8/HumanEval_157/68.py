```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of the triangle's right angle
    s = (a ** 2 + b ** 2) ** 0.5
    t = (a ** 2 + c ** 2) ** 0.5

    # Check if the length of the sides form a right-angled triangle
    return s == t or s == c or t == c
```

The function `right_angle_triangle` calculates the lengths of the two sides of the triangle's right angle, and then checks if the target length is equal to either of the two sides or the hypotenuse. The function passes test cases such as `right_angle_triangle(3, 4, 5)` returning True and `right_angle_triangle(1, 2, 3)` returning False. 

Another way to solve this problem is using the Pythagorean theorem, which states that, in a right triangle, the sum of the squares of the two shorter sides is equal to the square of the hypotenuse. The Pythagorean theorem can be expressed as:
```
a^2 + b^2 = c^2
```
In this approach, you can simply check the lengths of the two sides a and b against the length c, thereby determining if it is a right-angled triangle. 

It's important to note that the approach using the Pythagorean theorem is not optimized for performance, as it involves calculating the square root of the sum of squares, which has a higher time complexity compared to simple arithmetic operations. Hence, the first approach provided above is a more efficient way to determine a right-angled triangle.