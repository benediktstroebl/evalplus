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
    # Use built-in pow function with three arguments to calculate (2^n) % p
    # This is more efficient than using the ** operator and then the % operator
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

In this script, the `modp` function uses the `pow` function with three arguments to efficiently calculate `(2^n) % p`. The first argument to `pow` is the base, the second argument is the exponent, and the third argument is the modulus. This approach is more efficient than using the `**` operator and then the `%` operator.