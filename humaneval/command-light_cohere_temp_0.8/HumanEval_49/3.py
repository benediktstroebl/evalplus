```python
def modp(n, p): 
    """Return 2^n modulo p."""
    return pow(2, n, p) % p

# Unit tests
assert modp(3, 5) == 3
assert modp(1001, 101) == 2
assert modp(0, 101) == 1
assert modp(4, 11) == 8
assert modp(1000, 101) == 1
```
This function, `modp`, takes an integer `n` and a prime number `p` as input, and it returns the result of raising `2` to the `n` power and then taking the modulus `% p` to obtain the result.