```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power to which 2 should be raised.
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
    # Use the built-in pow function with three arguments to calculate (a^b) % c
    # This is more efficient than calculating a^b first and then taking the modulus
    return pow(2, n, p)

# Test the function
print(modp(3, 5))   # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))   # Expected output: 8
print(modp(100, 101)) # Expected output: 1
```

This script uses the `pow` function in Python, which can take three arguments: `a`, `b`, and `c`. It calculates `(a^b) % c` in constant time, making it much faster than calculating `a^b` first and then taking the modulus.