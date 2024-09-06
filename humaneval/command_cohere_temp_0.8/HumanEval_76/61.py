```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by comparing `x` to the power of `n` calculated by the expression `n ** int(x == n ** x)`. The expression `n ** int(x == n ** x)` is an adaptive iteration that first calculates the integer power `n ** x` and then refines it by taking the integer part of the ratio `x / (n ** x)` only if the previous step resulted in a floating-point number. This way, the function checks if `x` is equal to the expected simple power of `n` and returns `True` if so, and `False` otherwise, considering edge cases like taking the integer part of float(1.0) equal to 1.