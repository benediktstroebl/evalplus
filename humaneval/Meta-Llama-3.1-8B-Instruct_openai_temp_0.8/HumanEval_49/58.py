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
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:
            # If n is odd, multiply the result by base (2) modulo p
            result = (result * base) % p
        # Update base to be base squared modulo p for the next iteration
        base = (base * base) % p
        # Right shift n (divide by 2) to reduce the exponent
        n = n >> 1
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses a while loop to calculate 2^n modulo p efficiently by repeatedly squaring the base and reducing the exponent by half. The result is then updated by multiplying it by the base modulo p whenever the exponent is odd. This approach is more efficient than naive exponentiation when the exponents are large, as it reduces the number of multiplications required.