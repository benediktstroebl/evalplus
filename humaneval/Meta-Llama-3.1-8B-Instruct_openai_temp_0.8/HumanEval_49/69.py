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
    # Python's built-in pow function can handle modular exponentiation efficiently
    # We use the third argument to specify the modulus
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses Python's built-in `pow` function to efficiently compute the modular exponentiation. The `pow` function takes three arguments: the base, the exponent, and the modulus. It returns the result of the modular exponentiation, which is exactly what we need for this problem.