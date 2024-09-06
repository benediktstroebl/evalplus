```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The provided code defines a Python function called `is_simple_power` that takes two arguments, `x` and `n`. This function is designed to determine whether integer `n` is a simple power of number `x`. 

It returns "true" if the number `x` is a simple power of `n` and "false" otherwise. A number `x` is a simple power of `n` if `n` raised to the power of the integer value of `x` equals `x`. This condition is checked with the line `x == n ** int(x == n ** x)`. The integer value of `x` is checked using the `int()` function, and the triple equality `(x == n ** x)` checks if `x` equals `n` raised to the power of `x`.

The function also checks that `n` is an integer using the `type(n) is int` condition. This is to ensure that the function handles the case where `n` is not an integer correctly, as it should return false.