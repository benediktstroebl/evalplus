```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)
```

This function determines whether a given number `x` is a simple power of `n` by employing a straightforward equation. It checks if `x` is equal to `n` raised to the power of the integer obtained by taking the square root of `n`. This equation efficiently determines if `x` can be expressed as `n^k`, simplifying the determination of simple power relationships.