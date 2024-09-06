```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function `iscube` takes an integer `a` as input and returns `True` if `a` is a cube of some integer; otherwise, it returns `False`. This function first handles the negative case and then compares the absolute value of the input with the cube of the same integer to avoid taking floating-point values into account.