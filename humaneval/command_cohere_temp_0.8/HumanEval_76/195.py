```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It checks if the type of `n` is integer (returns `true` for int, long, IntegerType, etc.).
2. If `x` is equal to `n` raised to the power of `n` (simple power).
3. If `x` is equal to `n` raised to the power of `x` `== n**int(x)`.

Thus the function returns `true` if `x` is a simple power of `n` and `false` otherwise.

It is important to note that the definitive behavior of the function occurs in the `int(x == n * n)` portion of the logic. This ensures that the function can handle cases where `x` is not already in exponential form. 

For example:
- `is_simple_power(1, 4)` returns `true` since `4**2 == 4 ** int(4 * 4)`
- `is_simple_power(2, 2)` returns `true` since `2**2 == 2 ** int(2 * 2)`
- `is_simple_power(8, 2)` returns `true` since `8` is a simple power of `2` 
- `is_simple_power(3, 2)` returns `false` since `3` is not a simple power of `2`
- `is_simple_power(3, 1)` returns `false` since `3` is not a simple power of `1`
- `is_simple_power(5, 3)` returns `false` since `5` is not a simple power of `3`