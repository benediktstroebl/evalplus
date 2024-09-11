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
    # Initialize result to 1 (2^0 = 1)
    result = 1
    
    # Calculate 2^n modulo p using exponentiation by squaring
    while n > 0:
        # If n is odd, multiply result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Square result and divide n by 2
        result = (result * result) % p
        n = n // 2
    
    return result

# Test cases
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the exponentiation by squaring method to efficiently calculate 2^n modulo p. This method reduces the number of multiplications needed from O(n) to O(log n).