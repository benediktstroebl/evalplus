### Python Script to Calculate 2^n modulo p
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Args:
        n (int): The exponent.
        p (int): The modulus.

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
    result = 1
    # Use exponentiation by squaring to efficiently calculate 2^n
    while n > 0:
        if n % 2 == 1:
            # If n is odd, multiply the result by 2 modulo p
            result = (result * 2) % p
        n = n // 2  # Divide n by 2
    return result
```

You can run this script to test the function with different inputs.