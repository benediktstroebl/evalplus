```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the built-in pow function with three arguments to efficiently calculate (2^n) % p.
    This is more efficient than calculating 2^n and then taking the modulus.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of (2^n) % p.
    """
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script defines the `modp` function which takes two arguments `n` and `p`, and returns `(2^n) % p`. It uses the `pow` function with three arguments to efficiently calculate the result. The test cases at the end demonstrate the function's correctness.