### Modular Exponentiation
#### Python Script
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
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        # As we are doing integer division, we don't need to check for integer division by zero.
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script uses the property of modular arithmetic that `(a*b) mod n = ((a mod n) * (b mod n)) mod n`. This property allows us to avoid large intermediate results and calculate the result efficiently even for large values of `n`.