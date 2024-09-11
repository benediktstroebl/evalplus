### Modulo Power Function
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulo value.

    Returns:
        int: 2^n modulo p.

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
    result = 1  # Initialize result as 1
    base = 2  # The base is 2

    # We use the property of modular arithmetic that (a * b) % p = ((a % p) * (b % p)) % p
    # This helps us avoid large intermediate results
    while n > 0:
        # If n is odd, we multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # We divide n by 2 (n = n // 2) and move to the next iteration
        base = (base * base) % p
        n = n // 2

    return result
```
This script uses a modified version of the exponentiation by squaring algorithm to calculate `2^n modulo p` efficiently. It avoids large intermediate results by using the property of modular arithmetic.