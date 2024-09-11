### Modulo Power Function
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
    base = 2

    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n = n // 2

    return result
```
This script defines the `modp` function, which calculates 2^n modulo p using the exponentiation by squaring method. This method is more efficient than repeatedly multiplying 2 by itself n times, especially for large values of n. The function returns the result of this calculation.

Note that this function assumes that p is a prime number, as stated in the problem description. If p is not a prime number, the function may not work correctly.