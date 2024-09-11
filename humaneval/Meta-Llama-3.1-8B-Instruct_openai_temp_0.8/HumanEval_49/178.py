Here's a Python function to compute `2^n mod p` efficiently using the property of modular exponentiation:
```python
def modp(n: int, p: int) -> int:
    """
    Compute 2^n modulo p efficiently using modular exponentiation.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n mod p.

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
    base = 2
    while n > 0:
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square base and divide n by 2 for next iteration
        base = (base * base) % p
        n = n // 2
    return result
```
This function uses the property of modular exponentiation to efficiently compute `2^n mod p` by repeatedly squaring `2` and reducing the exponent `n` until it becomes 0. This approach avoids the need to compute the full value of `2^n` before reducing it modulo `p`.