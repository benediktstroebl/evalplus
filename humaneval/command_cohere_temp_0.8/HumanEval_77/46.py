```python
def iscube(a):
    # Check if the number is greater than 0 and equals to cube of some integer
    return a > 0 and a ** (1/3) == int(a ** (1/3))
```

This function `iscube()` checks if the number `a` is greater than 0 and verifies if it is a cube of some integer by evaluating `a ** (1/3)`. The expression `a ** (1/3)` returns the cube root of the number `a`. The function then converts the result of the cube root into an integer using `int()` and compares it with the original number `a`. If these two numbers are equal, it returns `True`; otherwise, it returns `False`.

The function assumes that the input is always valid, as stated in the problem statement. Thus, no further validation for negative cases or zero is applied.