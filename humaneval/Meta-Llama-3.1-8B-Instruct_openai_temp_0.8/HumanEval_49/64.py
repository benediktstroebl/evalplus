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
    # Initialize result to 1 (2^0)
    result = 1
    
    # Use exponentiation by squaring to efficiently compute 2^n
    base = 2
    while n > 0:
        # If n is odd, multiply the result by the current base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base
        base = (base * base) % p
        # Divide n by 2
        n = n // 2

    return result

# Test cases
print(modp(3, 5))     # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script uses the exponentiation by squaring technique to efficiently compute 2^n, which is the core operation in the modp function. The test cases at the end demonstrate the function's correctness.