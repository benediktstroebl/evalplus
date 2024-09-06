```python
def iscube(a):
    # Check if the integer a is a perfect cube
    b = a**(1/3)
    return round(b) == b
```

This function `iscube()` takes an integer `a` as input and checks if it is a perfect cube using the integer `b = a**(1/3)`. It then returns `True` if `b` is an integer, and `False` otherwise, satisfying the boolean values desired in the test cases.