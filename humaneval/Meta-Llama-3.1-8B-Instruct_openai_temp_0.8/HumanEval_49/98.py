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
    # Use the built-in pow function with three arguments to calculate (2^n) % p
    # This is more efficient and numerically stable than raising 2 to the power of n and then taking the modulus
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the `pow` function with three arguments to calculate (2^n) % p, which is more efficient and numerically stable than raising 2 to the power of n and then taking the modulus. The test cases are included at the end of the script to verify the function's behavior.