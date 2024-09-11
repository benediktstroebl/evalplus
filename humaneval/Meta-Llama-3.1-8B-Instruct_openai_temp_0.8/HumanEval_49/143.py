```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): exponent
    p (int): modulus
    
    Returns:
    int: 2^n modulo p
    """
    def power_mod(base: int, exponent: int, modulus: int) -> int:
        """
        Compute (base^exponent) % modulus efficiently.
        
        Args:
        base (int): base number
        exponent (int): exponent
        modulus (int): modulus
        
        Returns:
        int: (base^exponent) % modulus
        """
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            base = (base * base) % modulus
            exponent //= 2
        return result
    
    return power_mod(2, n, p)

# Test cases
print(modp(3, 5))     # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This code uses a helper function `power_mod` to efficiently compute the power modulo operation. The `modp` function uses this helper to calculate 2^n modulo p. The test cases are included at the end to demonstrate the function's correctness.