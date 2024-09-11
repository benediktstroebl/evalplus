```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The base number (2 in this case).
        p (int): The modulo number.

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
    while n > 0:
        # If n is odd, multiply the result by 2 (equivalent to 2^(n-1) * 2)
        if n % 2 == 1:
            result = (result * 2) % p
        # n must be even, so divide n by 2 (equivalent to n >>= 1)
        n = n >> 1
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```