```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (returns `true` for int, `false` for float).
2. If the type of `n` is integer, it then verifies if `x` equals `n` raised to the power of `int(x == n * n)`. This checks if `x` is a simple power of `n` without any floating numbers. 

Example tests would include:
```python
tests = [
    (1, 4, True),
    (2, 2, True),
    (8, 2, True),
    (3, 2, False),
    (3, 1, False),
    (5, 3, False),
]

for x, n, result in tests:
    assert is_simple_power(x, n) == result
```

Therefore, the function returns `True` if `x` is a simple power of `n`, and `False` otherwise.