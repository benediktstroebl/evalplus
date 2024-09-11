```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    :param n: The exponent
    :param p: The modulus
    :return: The result of 2^n modulo p
    """
    # Use the property of modular exponentiation that states:
    # (a*b) % n = ((a % n) * (b % n)) % n
    # This allows us to avoid large intermediate results
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular exponentiation to avoid large intermediate results. It repeatedly squares the base and divides the exponent by 2, multiplying the result by the base when the exponent is odd. This approach ensures that the result remains small and efficient, even for large exponents.