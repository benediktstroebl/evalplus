```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2 % p

    # Use exponentiation by squaring for efficient computation
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2

    return result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script defines the `modp` function to compute `2^n modulo p` efficiently using exponentiation by squaring, a common technique for fast modular exponentiation. The function takes two arguments, `n` and `p`, and returns the result of `2^n modulo p`. The test cases are included at the end to demonstrate the function's correctness.