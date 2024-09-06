```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by comparing `x` to the power of `n` calculated using both integer and non-integer exponentiation, and returns `True` if they are equal. It returns `False` if either exponentiation doesn't produce the same value or `n` is not an integer, indicating the original input is not a simple power.