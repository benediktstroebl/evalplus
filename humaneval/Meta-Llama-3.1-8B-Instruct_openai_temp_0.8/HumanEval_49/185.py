```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power to which 2 should be raised.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Divide n by 2
        n = n // 2
        # Update base to be the square of the current base
        base = (base * base) % p
    return result


# Test cases
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

This Python script defines a function `modp` that calculates `2^n modulo p` using the property of modular exponentiation, which is more efficient than calculating `2^n` first and then taking the modulus. The script also includes test cases to verify the correctness of the function.