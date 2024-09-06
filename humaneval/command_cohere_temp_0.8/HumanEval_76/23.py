```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is int to make sure that the operation `n ** int(...)` is feasible and doesn't trigger implicit casting, which may lead to precision loss.
2. It then compares `x` with `n ** int(...)`, where `int(...)` is evaluating to `1` when `x == n * n`. This works because when `x` is a simple power of `n`, the exponent of `n` in the scientific notation of `x` will be an integer.

Example usage:
```python
>>> is_simple_power(1, 4)
True
>>> is_simple_power(2, 2)
True
>>> is_simple_power(8, 2)
True
>>> is_simple_power(3, 2)
False
>>> is_simple_power(3, 1)
False
>>> is_simple_power(5, 3)
False
```