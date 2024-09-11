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
    base = 2 % p  # Precompute 2 modulo p to avoid repeated calculations
    
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p  # Multiply result by base and take modulus
        n = n // 2  # Divide n by 2
        base = (base * base) % p  # Square base and take modulus
    
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that calculates 2^n modulo p, where n is the exponent and p is the modulus. It uses a while loop to efficiently calculate the result by precomputing 2 modulo p and squaring the base at each iteration. The function returns the final result. The test cases at the end demonstrate the function's correctness.