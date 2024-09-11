```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n.
    This function uses exponentiation by squaring to efficiently calculate 2^n % p.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2 % p  # Reduce the base modulo p to avoid large numbers

    while n > 0:
        # If n is odd, multiply the current result by the base
        if n % 2 == 1:
            result = (result * base) % p

        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2

    return result


# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```

This script defines a function `modp` that calculates 2^n modulo p efficiently using exponentiation by squaring. The test cases are included to verify the function's correctness.