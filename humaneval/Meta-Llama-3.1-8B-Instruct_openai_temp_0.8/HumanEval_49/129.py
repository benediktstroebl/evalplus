```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

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
    # Initialize result to 1 (2^0 % p = 1)
    result = 1
    
    # Update result by multiplying it with base (2) and apply modular arithmetic
    for _ in range(n):
        result = (result * 2) % p
    
    return result
```

This script defines a function `modp` that calculates 2^n modulo p. It uses a loop to iteratively update the result by multiplying it with 2 and applying modular arithmetic, which is more efficient than raising 2 to the power of n directly.