### Modular Exponentiation with Python
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base number.
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
    base = 2
    while n > 0:
        # If n is odd, multiply the result with base
        if n % 2 == 1:
            result = (result * base) % p
        # n is even
        base = (base * base) % p
        n = n // 2
    return result
```
This Python script uses the property of modular exponentiation to efficiently calculate the result.