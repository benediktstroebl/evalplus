```python
def iscube(a):
    # Check if the number is equal to its cube root
    return a ** (1/3) == a
```

This function simply computes the cube root of the number `a` and compares it with `a` itself. Thus, it returns `True` if `a` is a perfect cube.