```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number (in this case, 2).
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments to calculate (2^p) mod p
    # This avoids potential numeric overflows and is more efficient
    return pow(2, n, p)


# Test cases
print(modp(3, 5))       # 3
print(modp(1101, 101)) # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script uses the built-in `pow` function with three arguments to efficiently calculate the result of `2^n` modulo `p`, avoiding potential numeric overflows.