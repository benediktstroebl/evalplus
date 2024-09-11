**Modular exponentiation using exponentiation by squaring**
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
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
    # Use exponentiation by squaring to efficiently compute 2^n
    while n > 0:
        # If n is odd, multiply the result by 2
        if n % 2 == 1:
            result = (result * 2) % p
        # Square 2 and divide n by 2
        n = n // 2
        # Update 2^n
        result = (result * result) % p
    return result
```
This script uses the exponentiation by squaring method to efficiently compute 2^n modulo p, which reduces the time complexity from O(n) to O(log n). The `modp` function takes two integers `n` and `p` as input and returns the result of 2^n modulo p.