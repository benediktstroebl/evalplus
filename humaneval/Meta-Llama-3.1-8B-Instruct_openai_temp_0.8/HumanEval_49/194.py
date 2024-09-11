### Python Script for Modular Exponentiation

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
    return pow(2, n, p)


# Test the function
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script uses Python's built-in `pow` function, which has a third argument for the modulus. This argument avoids large intermediate results, which can occur with naive implementations of modular exponentiation.