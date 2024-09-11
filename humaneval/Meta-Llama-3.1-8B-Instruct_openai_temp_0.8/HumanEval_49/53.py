### Modular Exponentiation using Python
```python
def modp(n: int, p: int) -> int:
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
    # Calculate 2^n using the fast modular exponentiation method
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result with base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2

    return result
```
This script defines a `modp` function that calculates 2^n modulo p using the fast modular exponentiation method. This method reduces the number of multiplications required, making it more efficient than naive implementations. The example use cases are included to demonstrate the function's behavior.