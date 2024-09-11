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
    power = 2
    while n > 0:
        # If n is odd, multiply the result by the current power of 2
        if n % 2 == 1:
            result = (result * power) % p
        # Square the current power of 2
        power = (power * power) % p
        # Divide n by 2
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the exponentiation by squaring method to efficiently calculate 2^n modulo p. This method reduces the number of multiplications required to calculate the result. The time complexity of this method is O(log n), where n is the exponent.