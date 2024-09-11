```python
def modp(n: int, p: int) -> int:
    """
    Calculate 2^n modulo p using the property of modular exponentiation.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p
    """
    # Use the property of modular exponentiation: (a*b) mod p = ((a mod p) * (b mod p)) mod p
    # Start with 2 and n, and repeatedly square 2 and n/2, until n becomes 0
    result = 1
    base = 2 % p  # Initial value of base
    while n > 0:
        # If n is odd, multiply the result by the current base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and halve n
        base = (base * base) % p
        n //= 2
    return result

# Test cases
print(modp(3, 5))       # 3
print(modp(1101, 101)) # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular exponentiation to efficiently calculate 2^n modulo p. It repeatedly squares the base (initially 2) and halves the exponent (initially n), adjusting the result at each step to ensure it remains accurate modulo p. This approach reduces the time complexity of the calculation to O(log n), making it much faster for large values of n.