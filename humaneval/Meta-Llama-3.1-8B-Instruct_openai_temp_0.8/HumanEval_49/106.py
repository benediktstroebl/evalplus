```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)


# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))   # 2
print(modp(0, 101))   # 1
print(modp(3, 11))   # 8
print(modp(100, 101))   # 1
```

This script uses the built-in `pow` function in Python, which has an optional third argument for the modulus. This is more efficient and numerically stable than manually calculating `2 ** n % p` for large values of `n` or `p`.