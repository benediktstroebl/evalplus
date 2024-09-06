```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `n` should be an integer.
2. If `x` is equal to `n` raised to the power of `int(x)`, then it is a simple power. Here, the int() function is used to remove the fractional part of the exponent.

This function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

You can test the above function inputting numbers "x" and "n" to see if the result is a simple power of "n".