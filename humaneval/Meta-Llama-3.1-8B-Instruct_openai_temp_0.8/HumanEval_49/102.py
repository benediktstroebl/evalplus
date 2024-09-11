### Modulus Power Function
#### A Python Function to Calculate 2^n Modulo p
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power of 2.
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
    base = 2

    # Use exponentiation by squaring for efficiency
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2

    return result
```
This script uses the **exponentiation by squaring** technique to efficiently calculate 2^n modulo p. This method reduces the number of calculations required to compute the modulus, especially for larger values of n.