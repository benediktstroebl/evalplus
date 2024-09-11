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
    while n > 0:
        # If n is odd, multiply result by 2 and take modulo p
        if n % 2!= 0:
            result = (result * 2) % p
        # Divide n by 2
        n = n // 2
    return result


# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This Python script uses the property of modular arithmetic that states `(a * b) mod p = ((a mod p) * (b mod p)) mod p`. The while loop simplifies the calculation of 2^n modulo p by dividing n by 2 in each iteration and updating the result accordingly. The `%` operator is used to take the modulo p of the result and/or the intermediate values.