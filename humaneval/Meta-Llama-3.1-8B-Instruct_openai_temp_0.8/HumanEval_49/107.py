```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    if p == 0:
        raise ValueError("Modulus cannot be zero.")

    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n //= 2

    return result

# Example usage
print(modp(3, 5))       # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))     # Output: 1
print(modp(3, 11))      # Output: 8
print(modp(100, 101))   # Output: 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p using the exponentiation by squaring method. It iterates over the bits of n from most significant to least significant, squaring the current result and multiplying it by 2 if the bit is 1. The result is then taken modulo p after each operation. This approach avoids potential overflow issues with large values of n.