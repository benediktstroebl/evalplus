```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether `n` is an integer and whether `x` equals `n` raised to the power of `x` (`n**int`). If these conditions are met, it returns `True`, otherwise, it returns `False`.