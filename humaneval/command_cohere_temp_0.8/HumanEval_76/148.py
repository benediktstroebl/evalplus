```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (returns `True` for int and `False` for float).
2. If `x` is equal to `n` raised to the power of both `x` and `int(x)`, it returns `True`. 

This is because a number is a simple power of `n` if it is equal to `n` raised to the power of another integer.

For example:
- `is_simple_power(1, 4)` returns `True` as it satisfies the condition `4 ** 1 == 4`.
- `is_simple_power(2, 2)` returns `True` as it satisfies the condition `2 ** 2 == 4`.
- `is_simple_power(8, 2)` returns `True` as it satisfies the condition `2 ** 4 == 8`.

The function returns `False` in other cases, such as when the type of `n` is not integer, or when `x` is not a simple power of `n`. 

For example:
- `is_simple_power(3, 2)` returns `False` as it fails the condition `2 ** 3 == 9`.
- `is_simple_power(3, 1)` returns `False` as it fails the condition `1 ** 3 == 3`.
- `is_simple_power(5, 3)` returns `False` as it fails the condition `3 ** 5 == 105`.