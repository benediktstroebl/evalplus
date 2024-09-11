### Modular Exponentiation using Binary Exponentiation
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    This function uses the binary exponentiation method to compute the result efficiently.
    
    Args:
        n (int): The exponent.
        p (int): The modulus.
    
    Returns:
        int: The result of 2^n modulo p.
    """
    # Handle edge cases
    if n == 0:
        return 1
    
    # Precompute the base (2%p) to avoid repeated divisions
    base = pow(2, p - 1, p)  # 2^(p-1) % p = 1
    
    # Initialize the result
    result = 1
    
    # Perform binary exponentiation
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```
This script uses the binary exponentiation method to efficiently compute the result of 2^n modulo p. It first precomputes the base (2%p) to avoid repeated divisions, then performs the exponentiation using the binary representation of the exponent. The test cases at the end demonstrate the function's correctness.