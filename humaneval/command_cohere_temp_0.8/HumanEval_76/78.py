```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It checks if the type of `n` is integer (returns `true` for int, long, IntegerWrapper, etc.).
2. If `x` is equal to `n` raised to the power of `x` (`n**int`).
3. Returns `true` if both conditions are satisfied and `false` otherwise. 

Such a simple solution is enough to solve this problem.