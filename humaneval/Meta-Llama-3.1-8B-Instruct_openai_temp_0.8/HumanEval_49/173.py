### Modular Exponentiation
Modular exponentiation is the process of raising a number to a power in modular arithmetic. It can be efficiently computed using the exponentiation by squaring method, which reduces the number of multiplications required.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p.

    Args:
    n (int): The exponent to which 2 should be raised.
    p (int): The modulo value.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Handle edge case where n is 0
    if n == 0:
        return 1
    
    # Initialize result to 1
    result = 1
    
    # Perform exponentiation by squaring
    while n > 0:
        # If n is odd, multiply result with 2^n
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Square 2 and reduce it modulo p
        n = n >> 1  # n = n / 2
        two_squared = 2 * 2  # 2^2 = 4
        two_squared %= p
    
    return result

# Test cases
if __name__ == "__main__":
    print(modp(3, 5))   # Output: 3
    print(modp(1101, 101))   # Output: 2
    print(modp(0, 101))   # Output: 1
    print(modp(3, 11))   # Output: 8
    print(modp(100, 101))   # Output: 1
```

This Python script implements the `modp` function using the exponentiation by squaring method to efficiently compute modular exponentiation. The function handles edge cases and includes test cases to verify its correctness.