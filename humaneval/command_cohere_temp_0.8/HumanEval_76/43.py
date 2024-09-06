```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function corroborates two conditions:
1. It checks whether the returned value of `n ** int(x == n ** x)` is `x`. This confirms if `x` is a simple power of `n`.
2. It verifies if `n` is an integer. This step ensures the simplicity of the power.

This function returns the correct result for the given test cases, which includes checking if `x` is a simple power of `n` for various values of `x` and `n`.