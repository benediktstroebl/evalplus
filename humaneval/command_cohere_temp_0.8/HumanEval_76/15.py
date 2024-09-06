```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function leverages the fact that if a number `x` is a simple power of `n` then it can be expressed as `n ** int(n ** 0.5)`. 

The expression `n ** int(n ** 0.5)` is a concise way of representing x raised to the power of the square root of `n` as an integer. It works by first calculating the square root of `n` and then rounding that value down to the nearest integer (using `int()`). This rounded value is then used as the exponent for `n`. 

By comparing `x` to `n ** int(n ** 0.5)`, the function correctly identifies whether `x` is a simple power of `n`.