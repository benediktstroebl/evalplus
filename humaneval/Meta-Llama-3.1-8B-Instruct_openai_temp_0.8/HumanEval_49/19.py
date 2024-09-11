```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    This function uses the property of modular exponentiation to efficiently calculate 2^n modulo p.
    
    :param n: The exponent (base 2)
    :param p: The modulus
    :return: 2^n modulo p
    """
    result = 1
    while n > 0:
        # If n is odd, multiply result by 2 and take modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # Square result and take modulo p
        result = (result * result) % p
        # Right shift n by 1 bit (divide by 2)
        n = n >> 1
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script uses the property of modular exponentiation to efficiently calculate 2^n modulo p. The time complexity is O(log n), which is much better than the naive approach of calculating 2^n and then taking modulo p, which would have a time complexity of O(n).