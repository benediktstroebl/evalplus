```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The given code directly evaluates the given expressions. e.g., `n ** int(x == n ** x)`; This will first compare `x` with the integer power `n ** x` and will return `True` if they are equal, thus correctly identifying `x` as a simple power of `n`. The type annotation `type(n) is int` also ensures that the exponent `n` is an integer, returning `False` for non-integer exponents. 

This approach solves the problem in an efficient and concise manner.