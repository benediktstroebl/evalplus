```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    # Initialize result to 1, as any number to the power of 0 is 1
    result = 1
    
    # Use exponentiation by squaring for efficient computation
    while n > 0:
        # If n is odd, multiply result by 2
        if n % 2 == 1:
            result = (result * 2) % p
        # Double 2^n
        n = n // 2
        # Reduce p by 1 each time we double n, to avoid overflow
        # (2^n % p) % p = (2^(n % (p-1)) % p)
        p = p - 1
    
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```
This script uses the exponentiation by squaring technique to efficiently calculate `2^n modulo p`. The time complexity is O(log n), making it much faster than naive approaches for large inputs. The space complexity is O(1), as we only use a constant amount of space to store the result and the power.