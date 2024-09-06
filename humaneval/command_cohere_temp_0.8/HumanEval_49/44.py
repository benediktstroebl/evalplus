```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` is defined to return the value of `2` raised to the power of `n` and then taken modulo `p`. This is achieved by using the built-in Python function `pow`, which calculates `x` raised to the power of `y`, and could be used to solve this problem simply as `pow(2, n, p)`.