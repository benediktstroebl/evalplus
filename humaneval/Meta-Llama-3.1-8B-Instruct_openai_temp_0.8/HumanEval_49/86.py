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
    for _ in range(abs(n)):
        result = (result * 2) % p
    return result if n >= 0 else -result

# Test cases
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```

This script defines a function `modp` that calculates the value of 2 raised to the power `n` and then takes the modulus with `p`. It handles negative exponents by making the result negative if `n` is negative. The script then includes the provided test cases to demonstrate the function's behavior.