```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer by simply computing the cube of `a` and comparing it with the original input. If they are the same, then it returns `True`, else `False`. The special case of `a < 0` is considered by transforming it to its positive equivalent `(-a)` and then performing the cube operation. 

This approach assumes that the input is always valid, as stated in the note in the problem statement.