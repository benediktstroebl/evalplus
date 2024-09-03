```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p, handles numerics properly.

    Args:
        n (int): Exponent.
        p (int): Modulus.

    Returns:
        int: 2^n modulo p.
    """
    return pow(2, n, p)
```