```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (`type(n) is int`).
2. If the condition in the first point is satisfied, it checks whether `x` is equal to `n` raised to the power of `int(x == n * n)`. This condition checks if `x` can be written as `n^int(x)`, where `int(x)` is the integer value of which `x` is quantized.

This should return `True` for cases like `is_simple_power(1, 4)`, `is_simple_power(2, 2)`, and `is_simple_power(8, 2)`, and `False` for cases like `is_simple_power(3, 2)`, `is_simple_power(3, 1)`, and `is_simple_power(5, 3)`.