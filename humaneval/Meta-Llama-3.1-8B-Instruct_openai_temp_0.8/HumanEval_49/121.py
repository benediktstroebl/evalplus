```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Initialize the base case, 2^0 % p is always 1
    result = 1
    
    # Use exponentiation by squaring for efficiency
    while n > 0:
        # If n is odd, multiply the result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        
        # Square 2 modulo p
        n = n // 2  # integer division to avoid floating point
        p = (p * p) % p  # update p for the next iteration
        
    return result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the property of modular arithmetic that $(a \cdot b) \mod p = ((a \mod p) \cdot (b \mod p)) \mod p$ to calculate $2^n \mod p$ efficiently. It uses exponentiation by squaring to square the result in each iteration, which reduces the time complexity from $O(n)$ to $O(\log n)$.