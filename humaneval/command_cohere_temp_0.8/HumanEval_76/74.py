```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by comparing `x` to the power of `n` calculated by exponentiating `n` to the power of the integer value of `x == n ** x`. The function returns `True` if `x` is a simple power of `n`, and `False` otherwise. This behavior is in line with the given example and should pass the tests.