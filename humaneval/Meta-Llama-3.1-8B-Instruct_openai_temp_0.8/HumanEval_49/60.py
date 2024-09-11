```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    
    Example:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
    return result
```

This script uses the concept of modular exponentiation to calculate `2^n modulo p`. It iteratively halves the exponent and doubles the result modulo p, which makes the process more efficient and avoids large intermediate results.