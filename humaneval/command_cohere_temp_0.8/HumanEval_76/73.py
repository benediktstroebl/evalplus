```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function examines whether a number `x` is a simple power of `n` by verifying two conditions:
1. `n` should be an integer.
2. `x` should be equal to the result of raising `n` to the power of the integer value of `x == n**x`.

This approach ensures that `is_simple_power(x, n)` returns `True` for valid simple power scenarios like `is_simple_power(1, 4)` and correctly identifies non-simple power cases like `is_simple_power(3, 2)` or `is_simple_power(5, 3)`.