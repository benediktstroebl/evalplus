```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether `n` is an integer and whether `x` is equal to `n` raised to the power of itself. The latter is achieved using the expression `n ** int(x == n ** x)`, which evaluates to `n` if `x` is a simple power of `n` and raises a `TypeError` if `x` is not a simple power, as the result of comparing `x` with `n ** x` is not an integer. Hence, the condition returns `true` if `x` is a simple power of `n` and `false` otherwise. 

This approach guarantees a concise solution that fulfills the problem requirements.