```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Parameters:
    n (int): exponent
    p (int): modulus
    
    Returns:
    int: 2^n modulo p
    
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
    while n > 0:
        # If n is odd, add the base to the result
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This Python script uses the property of modular arithmetic that states `(a*b) mod p = ((a mod p) * (b mod p)) mod p`. This property is used to calculate `2^n mod p` without calculating `2^n` first, which can be very large. The script uses a while loop to repeatedly square the base (`2`) and divide the exponent (`n`) by 2 until `n` is 0. When `n` is odd, the base is added to the result. The result is calculated modulo `p` at each step to prevent large intermediate results.