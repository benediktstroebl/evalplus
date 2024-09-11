```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that 
    (a*b) % n = ((a % n) * (b % n)) % n to avoid overflow.

    Args:
        n (int): The base number.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2
    
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        
        # Square the base and reduce modulo p
        base = (base * base) % p
        
        # Right shift the bits of n to divide it by 2
        n = n >> 1
    
    return result

# Test cases
print(modp(3, 5))   # Expected output: 3
print(modp(1101, 101))   # Expected output: 2
print(modp(0, 101))   # Expected output: 1
print(modp(3, 11))   # Expected output: 8
print(modp(100, 101))   # Expected output: 1
```

This script defines a function `modp` that calculates 2^n modulo p without overflowing. It uses a while loop to divide n by 2 in each iteration, multiply the result by the base (2) if n is odd, and square the base modulo p. The function returns the final result, which is 2^n modulo p. The test cases are included at the end of the script to verify the correctness of the function.