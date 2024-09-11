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
    result = 1  # Initialize result to 1
    base = 2  # The base number
    while n > 0:  # Continue until n becomes 0
        if n % 2 == 1:  # If n is odd
            result = (result * base) % p  # Multiply result by base and take modulus p
        n = n // 2  # Divide n by 2
        base = (base * base) % p  # Update base to be base squared and take modulus p
    return result  # Return the final result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script implements the `modp` function as specified and includes test cases to verify its correctness. The function uses a binary exponentiation technique to efficiently compute 2^n modulo p, which is useful for large exponents.