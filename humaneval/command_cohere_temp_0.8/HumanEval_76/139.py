```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The given function checks if the number `x` is a simple power of `n` and returns `True` if it is and `False` otherwise. It does so by taking two arguments, `x` and `n`, and it returns a boolean that tells us if x is a simple power of n or not. It works by checking if `x` is equal to `n` raised to the power of `x` (which is an integer). From the MD code block, it passes the test cases of 1, 2, 8, and fails the test cases 3, 5, and others.