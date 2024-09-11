```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments to efficiently compute the power modulo p
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the `pow` function with three arguments to efficiently compute the power modulo p, which is faster and more numerically stable than using the `**` operator or a loop. The `pow` function returns the result of `a` raised to the power `b`, modulo `c` when called with three arguments.