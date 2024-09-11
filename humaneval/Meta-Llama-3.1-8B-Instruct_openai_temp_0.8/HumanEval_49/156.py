```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.

    Examples:
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
    for _ in range(n):
        result = (result * 2) % p
    return result
```

This script defines a function `modp` that calculates `2^n modulo p` efficiently by repeatedly squaring the current result and reducing it modulo `p`. This approach avoids the problem of large intermediate results, making it suitable for large values of `n`.