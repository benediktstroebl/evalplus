```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
        n (int): The power of 2.
        p (int): The modulo value.
    
    Returns:
        int: The result of 2^n modulo p.
    
    Examples:
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
        if n % 2 == 1:  # If the current bit is 1
            result = (result * base) % p
        n = n // 2  # Divide the current power by 2
        base = (base * base) % p  # Update the base for the next iteration
    return result

# Test the function
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the exponentiation by squaring method to efficiently calculate 2^n modulo p. It handles large values of n and p by reducing the modulo operation at each step, thus avoiding overflow. The test cases are included at the end to demonstrate the function's correctness.