```python
def modp(n: int, p: int) -> int:
    """
    Returns 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        # n is even, apply modpow recursively
        return modp(n // 2, p) * modp(n // 2, p) % p
    else:
        # n is odd, apply modpow recursively and multiply by 2
        return 2 * modp(n // 2, p) * modp(n // 2, p) % p

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This implementation uses a recursive approach to calculate 2^n modulo p, taking advantage of the property that (a*b) mod p = ((a mod p) * (b mod p)) mod p. This helps to avoid large intermediate results and prevent potential overflow issues.