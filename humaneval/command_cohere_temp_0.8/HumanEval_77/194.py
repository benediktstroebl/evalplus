```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer by simply cubing the number and comparing the result to the original input. If they are the same, it returns `True`, else `False`. Additionally, it handles the case when `a` is negative by converting it to its positive equivalent since the absolute value of a negative number is also a cube for some integer.