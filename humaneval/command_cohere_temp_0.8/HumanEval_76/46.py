```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function checks if a given number `x` is a simple power of `n` by comparing it with the result of raising `n` to the power of `int(n ** 0.5)`, which represents the largest integer power of `n` that can produce `x`. The function returns `True` if `x` is a simple power of `n`, and `False` otherwise.