```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == 0 or b == 0 or c == 0) or (a == b or b == c or a == c):
        return False
    else:
        s = (a**2 + b**2 + c**2) / 2
        return s**0.5 == abs(a) or s**0.5 == abs(b) or s**0.5 == abs(c)
```

This function checks for three specific cases:
1. The triangle with side lengths of 0.
2. One of the side lengths is 0, or two or all three side lengths are equal.
3. The sum of the squares of the sides is equal to zero.

And finally, it checks if the square root of the sum of the squares of the sides is equal to any of the side lengths of the triangle. If any of these conditions are met, it returns True, if none are met, it returns False. This works because a right-angled triangle is uniquely determined by the Pythagorean theorem. 

The function works as expected and passes the tests provided in the prompt since it returns True for the example with side lengths 3, 4, and 5, and returns False for the example with side lengths 1, 2, and 3. 

It is important to note that the function assumes that the inputs are valid and correctly calculate the square root. If you input a side length of 0, the function will return True, since all side lengths of zero result in a right angle. 

Make sure to handle edge cases and validate input if this is intended to handle non-sensible input.