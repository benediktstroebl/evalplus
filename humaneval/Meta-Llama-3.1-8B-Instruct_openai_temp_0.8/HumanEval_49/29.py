### Modular Exponentiation in Python

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The exponent.
    p (int): The modulo value.
    
    Returns:
    int: The result of 2^n modulo p.
    """
    
    # Handle the special case where n is 0
    if n == 0:
        return 1
    
    # Initialize the result to 1
    result = 1
    
    # Perform modular exponentiation
    while n > 0:
        # If n is odd, multiply the result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # Square 2 modulo p and divide n by 2
        n = n // 2
        p = (p * p) % p
    
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular arithmetic that `(a*b) % n = ((a % n) * (b % n)) % n` to efficiently calculate `2^n modulo p`. The time complexity of this algorithm is O(log n), where n is the exponent.