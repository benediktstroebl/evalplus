```python
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    
    This function uses the property of modular exponentiation to efficiently
    calculate 2^n modulo p.
    
    Args:
        n (int): The exponent.
        p (int): The modulus.
    
    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2
    
    # Use exponentiation by squaring to efficiently calculate the power
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        
        # Square the base and divide n by 2
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

This script uses the property of modular exponentiation to efficiently calculate 2^n modulo p. It uses a while loop to repeatedly square the base and multiply the result by the base if n is odd, effectively calculating 2^n modulo p.