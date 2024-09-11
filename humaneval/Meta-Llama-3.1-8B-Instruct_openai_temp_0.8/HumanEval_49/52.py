```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    This function uses the property of modular arithmetic that 
    (a * b) % p = ((a % p) * (b % p)) % p.
    
    Args:
        n (int): The exponent.
        p (int): The modulus.
    
    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            # Use modular arithmetic to avoid large numbers
            result = (result * base) % p
        # Square the base and reduce it modulo p
        base = (base * base) % p
        # Divide n by 2
        n = n // 2
    return result

# Test cases
print(modp(3, 5))        # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))      # 1
print(modp(3, 11))       # 8
print(modp(100, 101))    # 1
```

This script uses the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p` to avoid large numbers. The time complexity of this script is O(log n), making it efficient for large values of `n`.