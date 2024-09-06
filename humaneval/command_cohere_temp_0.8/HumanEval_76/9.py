```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating the condition `n ** int(x == n ** x)`. It returns `True` if `x` is a simple power of `n` and `False` otherwise.