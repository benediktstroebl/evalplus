```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the built-in pow function with three arguments
    to efficiently calculate 2^n modulo p.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.
    """
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the `pow` function with three arguments to calculate `2^n modulo p`. The `pow` function can take up to three arguments: `a`, `b`, and `c`. When `c` is specified, it returns `a` raised to the power of `b` modulo `c`. This approach is more efficient than repeatedly multiplying `2` by itself and taking the modulus at each step.