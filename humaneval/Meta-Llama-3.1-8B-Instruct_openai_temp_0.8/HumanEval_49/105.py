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
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base (2)
        if n % 2 == 1:
            result = (result * base) % p
        # n is even, divide it by 2
        n = n // 2
        # Update base to be the square of the current base (base^2)
        base = (base * base) % p
    return result

# Test the function with the provided examples
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p`. It calculates `2^n` modulo `p` by iteratively squaring the base (`base = base * base % p`) and updating the result when `n` is odd. The result is then returned modulo `p`.