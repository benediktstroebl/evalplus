### Modular Exponentiation using Binary Exponentiation
#### Problem: Compute 2^n modulo p efficiently.

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    The function uses binary exponentiation to compute the result efficiently.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Handle edge cases
    if n == 0:
        return 1
    
    # Initialize result to 1
    res = 1
    
    # 2 raised to the power 1 is 2
    base = 2
    
    # Perform binary exponentiation
    while n > 0:
        # If n is odd, multiply base to result
        if n % 2 == 1:
            res = (res * base) % p
        
        # Square base and halve n
        base = (base * base) % p
        n = n // 2
    
    # Return the result
    return res

# Test cases
print(modp(3, 5)) # 3
print(modp(1101, 101)) # 2
print(modp(0, 101)) # 1
print(modp(3, 11)) # 8
print(modp(100, 101)) # 1
```

This script uses the binary exponentiation technique to compute 2^n modulo p efficiently. It starts with a base of 2 and squares it repeatedly while halving the exponent until the exponent becomes 0. The result is then calculated by multiplying the result with the base whenever the exponent is odd. This approach reduces the number of multiplications required, making it more efficient than the naive approach of repeated multiplication.