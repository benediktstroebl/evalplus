```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function leverages the property that if a is a cube of an integer n then a ** 3 will be an integer, i.e. = `a ** 3 == int(a ** 3)` and also handles the case when a is negative, since `-a` is a cube of `-1`.