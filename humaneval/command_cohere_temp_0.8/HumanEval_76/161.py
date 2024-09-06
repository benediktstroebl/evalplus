```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It checks if the type of `n` is integer (returns `true` for int, long, float, complex) to make sure that the operation int() is valid for `n` and `x`.
2. It checks if `x == n * n` to see if `x` is the square of `n`.
3. It also checks if `x == n ** int(x == n * n)` to see if `x` is a simple power of `n`. The int() function converts the result of the exponential expression to an integer, so if `x` is a simple power of `n`, this condition will be true.

The function returns `true` if `x` is a simple power of `n` and false in other cases. It handles cases like 1, 2, 8 which are simple powers and also takes into account cases like 3, 5, false positives like 2, which are not simple powers.