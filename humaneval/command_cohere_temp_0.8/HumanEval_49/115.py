```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` uses the `pow` function to calculate `2` raised to the power of `n` modulo `p`. This expression is mathematically equivalent to what is described in the problem statement.

The function is self-contained and does not require any additional imports or dependencies. It is also concise and achieves the desired result with a single line of code.

If you want to make it more robust, you could add some input validation, like checking if `n` and `p` are integers, and `p` is a positive number. Also, it's worth noting that the `pow` function in Python 3 automatically handles negative exponents, so there's no need to explicitly check for that case. Here's a slightly enhanced version:
```python
def modp(n, p):
    if not isinstance(n, int) or not isinstance(p, int) or p <= 0:
        raise ValueError("Input must be positive integers")
    return pow(2, n, p)
```