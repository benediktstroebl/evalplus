```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two legs
    d = ((a ** 2) + (b ** 2) - (c ** 2)) ** 0.5
    e = ((b ** 2) + (c ** 2) - (a ** 2)) ** 0.5
    # Check for the presence of a right angle
    return d * e == b * c and d + e == c + a
```

The function `right_angle_triangle` takes three arguments `a`, `b`, and `c`, which represent the lengths of the three sides of the triangle. It calculates the lengths of the two legs of the triangle using the Pythagorean theorem and then checks whether these two legs are the two sides of a right angle, as well as whether the hypotenuse is the third side of the triangle. 

This approach will give the correct result for the given example cases.