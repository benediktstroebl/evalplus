```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether `n` is an integer and whether `x` equals `n` raised to the power of `x` (`n**int`). The latter is achieved by using the expression `x == n ** x` to determine if `x` is a simple power of `n`.