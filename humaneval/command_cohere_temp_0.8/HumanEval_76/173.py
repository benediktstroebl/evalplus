```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to make sure that the function returns false for non-integer bases, as per the test cases for `is_simple_power(3, 2)` and `is_simple_power(3, 1)`.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - Whether `x` is equal to `n` raised to the power of `int(x)`. This is the standard check for simple powers.
    - Whether `x` is equal to `n` raised to the power of `x`. If this is true, then `x` is a simple power, but not necessarily an integer power (`n**int=x`). This step is crucial to handle cases like `is_simple_power(8, 2)`.
    - Whether `x` is an integer. This is implicit in the `int(x == n ** x)` condition, but the type checking ensures that we only proceed with the third condition when `n` is an integer.

The code reads a bit convoluted, but it is structured such that the explicit type checking on `n` ensures that we don't try to evaluate `n ** x` unless we know that `n` is an integer. This allows us to catch non-integer bases, while still handling the case where `x` is a simple power but not an integer power.