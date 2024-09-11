```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): Exponent.
        p (int): Modulus.

    Returns:
        int: 2^n modulo p.
    """
    # Use built-in pow function with three arguments to handle modular exponentiation
    # The third argument is the modulus, which prevents overflow
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the `pow` function with three arguments to handle modular exponentiation, which is more efficient and numerically stable than repeated multiplication modulo `p`.