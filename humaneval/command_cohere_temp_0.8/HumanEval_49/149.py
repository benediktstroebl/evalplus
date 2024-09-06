```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` is defined to solve the problem of computing `2^n modulo p` where it uses the built-in Python function `pow()` to compute the power of `2` and then take the result modulo `p`. This solution is concise and efficient.

This solution assumes n and p are already given as input to the function in that order.