```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base (2 in this case)
    p (int): The modulus

    Returns:
    int: The result of 2^n modulo p
    """
    result = 1
    # Use exponentiation by squaring for efficient calculation
    while n > 0:
        # If n is odd, multiply result by 2 modulo p
        if n % 2 == 1:
            result = (result * 2) % p
        # Square 2 modulo p and divide n by 2
        n = n // 2
        p = (p * p) % p  # Use modulus to prevent overflow
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```

This script uses exponentiation by squaring, a common technique for efficiently calculating large powers. It also uses the modulus operator to prevent overflow when dealing with large numbers. The time complexity of this algorithm is O(log n), making it much more efficient than naive approaches for large inputs.