```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power to which 2 is raised.
    p (int): The modulo value.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use Python's built-in pow function with three arguments to calculate the power modulo p
    # to avoid large intermediate results
    return pow(2, n, p)


# Test cases
print(modp(3, 5))   # Expected output: 3
print(modp(1101, 101))   # Expected output: 2
print(modp(0, 101))   # Expected output: 1
print(modp(3, 11))   # Expected output: 8
print(modp(100, 101))   # Expected output: 1
```

In this script, we use Python's built-in `pow` function to calculate `2^n modulo p`. The `pow` function takes three arguments: the base, the exponent, and the modulo value. This allows us to calculate the power modulo p directly, avoiding large intermediate results.