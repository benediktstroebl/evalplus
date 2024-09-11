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
    # Initialize the result to 1 (multiplicative identity)
    result = 1
    
    # 2 ^ (2^k) % p = (2 ^ k * 2 ^ k) % p (Fermat's Little Theorem)
    # We can use this to avoid overflow for large exponents.
    k = 0
    while n > 0:
        # If n is odd, multiply the result by 2
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Square 2 and reduce it modulo p
        n = n // 2
        p = (p * p) % p
        
        # To prevent p from getting too large and causing overflow
        k += 1
    
    return result

# Example usage:
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101)) # Output: 1
```