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
    result = 1  # Initialize result to 1
    base = 2  # Use 2 as the base (2^n)
    while n > 0:  # Continue while n is greater than 0
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # n is even, so divide n by 2
        base = (base * base) % p
        n = n // 2  # Same as n //= 2
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script uses a loop to compute 2^n modulo p efficiently using the properties of modular arithmetic. The time complexity is O(log n), where n is the exponent. The function returns the result as an integer.