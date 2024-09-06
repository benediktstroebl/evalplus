```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n % p` by leveraging the built-in function `pow(x, y, p)`, which works for positive integers `x`, `y`, and `p`; the latter two should be free of common pitfalls such as being negative or exponentiating to an overly large number. This function is equipped with unit tests expected to pass:
```python
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
```

When specifying the arguments for this function, ensure:
- `n` and `p` are positive integers.
- Avoid numeric pitfalls like `p` being a prime number.

This function promptly returns the desired result with an elegant utilization of built-in functions, sans the nuances associated with manual exponentiation.