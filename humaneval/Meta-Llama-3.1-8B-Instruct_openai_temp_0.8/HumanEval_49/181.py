```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    This function calculates the power of 2 modulo p using the property of modular exponentiation.
    
    Args:
        n (int): The power to which 2 is to be raised.
        p (int): The modulo value.
    
    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2
    
    # Use exponentiation by squaring for efficient calculation
    while n > 0:
        # If n is odd, multiply the result with base
        if n % 2 == 1:
            result = (result * base) % p
        
        # Square the base and reduce it modulo p
        base = (base * base) % p
        
        # Right shift n by 1 bit (divide n by 2)
        n = n >> 1
    
    return result

# Example usage
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```

This script defines a function `modp` that calculates 2^n modulo p using the property of modular exponentiation. It uses the exponentiation by squaring method for efficient calculation. The example usage at the end demonstrates the function's behavior with different inputs.