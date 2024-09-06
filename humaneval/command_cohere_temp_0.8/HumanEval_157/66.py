```python
def right_angle_triangle(a, b, c):
    if a == c or b == c or a == b:
        return True
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return True
    else:
        return False
```

This function checks the triangle sides using the Pythagoras theorem, as well as some edge cases like when two sides are equal or when a side is equal to the third side. 

To ensure this function works for any set of sides, you might want to add more test cases to cover other edge cases and corner scenarios. 

The problem can be approached like this because the Pythagoras theorem is a fundamental definition in mathematics, assuming the inputs are being measured in standardized units compatible with this formula, namely that they are all in terms of Euclidean distance i.e. linear measurements.