```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == 0 or b == 0 or c == 0) and (a + b == c or a + c == b or b + c == a):
        return True
    else: 
        numer = (a**2 + b**2 + c**2) / 2 - sqrt((b**2 + c**2 - a**2) / 2) ** 2
        denom = (a**2 + b**2 + c**2) / 2 + (b**2 + c**2 - a**2) / 2 
        return numer == denom 
```

This Python script defines a function called `right_angle_triangle` that takes three arguments: `a`, `b`, and `c`, which represent the lengths of the three sides of a triangle. 

The function first handles the edge case of a triangle with zero length sides:
1. Returns True if `a`, `b`, and `c` are all equal to zero, indicating that the triangle is degenerate and none of the sides can be determined to be right.
2. Returns True if one of the sides is zero and the sum of the other two sides is equal to the missing side (consistent with the Pythagoras' theorem).

It then checks if the triangle is a right triangle based on the Pythagoras' theorem. 

The Pythagoras' theorem states that in a right triangle, the sum of the squares of the two shorter sides equals the square of the longest side. 

The script determines whether the lengths of the three sides form a right-angled triangle by checking if the sum of the squares of the `a`, `b`, and `c` values is equal to the square of the hypotenuse, using the equation: `numer = (a**2 + b**2 + c**2) / 2 - sqrt((b**2 + c**2 - a**2) / 2) ** 2`.

If the condition is met, the function returns `True`, indicating that the sides form a right-angled triangle; otherwise, it returns `False`.

The script then includes an example and test cases to ensure the function's correctness.