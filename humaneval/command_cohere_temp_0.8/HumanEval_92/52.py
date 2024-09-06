```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z

    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

This function checks if any of the sums of pairs of the input variables are equal to the third number. Then it checks if the returned sums and the third number are integers, and finally returns a boolean that answers the question.

It can be improved to support more edge cases, such as floating-point numbers.