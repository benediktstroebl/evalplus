```python
def iscube(a):
    if a < 0:
        a = -a
    return a ** 3 == int(a ** 3)
```

This function `iscube()` checks if the given integer `a` is a cube of some integer number. The function first handles the case when the input `a` is negative by making it positive, then it returns `True` if `a` **is a power of 3** (i.e., `a` equals `n * 3^k` for some integers `n` and `k`); otherwise, it returns `False`. 

The function assumes that the input is always valid, as stated in the problem statement. Therefore it does not need to check for edge cases like `NaN`, `inf`, or values less than 0.