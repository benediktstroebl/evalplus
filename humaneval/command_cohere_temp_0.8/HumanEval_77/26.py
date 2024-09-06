```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer by simply cubing the number and comparing the result to the original input. If they are the same, it returns `True`, else `False`. The condition `if a < 0` handles the case for negative numbers, as the cubing operation for negative numbers yields a negative number, but for the purpose of this problem, we need to return True for negative cubes as well.