```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulo.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use the built-in pow function with three arguments to calculate the power modulo p
    # This is more numerically stable than (2 ** n) % p
    return pow(2, n, p)


# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that calculates `2^n modulo p` using the `pow` function with three arguments, which is more numerically stable than the naive approach of calculating `(2 ** n) % p`. The script then includes test cases to demonstrate the function's correctness.