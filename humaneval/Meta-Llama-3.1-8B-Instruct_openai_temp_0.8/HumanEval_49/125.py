```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.

    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    # Calculate 2^n using the built-in pow function with three arguments
    # The third argument is the modulus, which avoids large intermediate results
    result = pow(2, n, p)
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the `pow` function with three arguments to calculate 2^n modulo p efficiently, avoiding large intermediate results. The `pow` function is more efficient and numerically stable than calculating the power directly using exponentiation.