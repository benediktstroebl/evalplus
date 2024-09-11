```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.

    Example usage:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    
    # Calculate 2^n
    result = 1
    two = 2
    
    # Use exponentiation by squaring to efficiently compute 2^n
    while n > 0:
        # If n is odd, multiply result by 2
        if n % 2 == 1:
            result = (result * two) % p
        
        # Square 2 and divide n by 2
        two = (two * two) % p
        n = n // 2
    
    return result

# Test the function
print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))
```

This script uses the exponentiation by squaring technique to efficiently compute 2^n modulo p. This method has a time complexity of O(log n), making it more efficient than simply computing 2^n and then taking the modulus, which would have a time complexity of O(n).