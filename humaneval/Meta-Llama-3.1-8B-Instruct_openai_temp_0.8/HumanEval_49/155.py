```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
        n (int): exponent
        p (int): modulus
    
    Returns:
        int: result of 2^n modulo p
    
    Example:
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
    result = 1
    base = 2
    
    # Use exponentiation by squaring for efficient computation
    while n > 0:
        if n % 2 == 1:  # if n is odd
            result = (result * base) % p
        
        # square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    
    return result

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script defines a function `modp` that efficiently computes 2^n modulo p using exponentiation by squaring. The test cases at the end of the script run the function with the provided examples and assert that the results match the expected outputs.