```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The power to which 2 should be raised.
    p (int): The modulo to apply to the result.
    
    Returns:
    int: The result of 2^n modulo p.
    """
    result = 1
    while n > 0:
        # If n is odd, multiply the result by 2
        if n % 2 == 1:
            result = (result * 2) % p
        # Divide n by 2
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script uses the property of modular arithmetic that `(a*b) % p = ((a % p) * (b % p)) % p` to efficiently calculate `2^n` modulo `p` without dealing with large numbers. The script repeatedly squares the result (to keep the calculation in the range of `p`) and applies the modulo operation until `n` becomes 0.