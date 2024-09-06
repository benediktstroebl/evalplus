```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer. It starts by handling the negative case by converting it to its positive equivalent (`a = -a`). Then, it checks if `a` is a cube of an integer by taking its cube root and comparing it to an integer value. The result is then returned as a boolean True or False.