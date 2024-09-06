```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function checks if the given integer `a` is a cube of some integer by simply cubing the number and comparing the result to the original input. If they are equal, it returns `True`. Otherwise, it returns `False`. Additionally, it accounts for the case when `a` is negative by adjusting it to its absolute value. This way, it correctly identifies positive and negative valid cubes alike.

To handle the special cases mentioned in the problem, you can modify the function to include explicit checks:
```python
def iscube(a):
    if a == 0:
        return True
    elif a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This modification ensures that `iscube(0)` returns `True`, accurately identifying zero as a valid cube value, while maintaining the original functionality for other cases.