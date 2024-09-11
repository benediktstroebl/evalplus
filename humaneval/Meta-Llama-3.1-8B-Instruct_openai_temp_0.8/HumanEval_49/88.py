### Modp Function in Python
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
    # Use the built-in pow function with three arguments (base, exponent, modulus)
    # to calculate 2^n modulo p efficiently.
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```
This script defines a function `modp` that calculates 2^n modulo p using the `pow` function. The `pow` function with three arguments is more efficient than using the modulo operator `%` because it avoids unnecessary intermediate results. The test cases are included at the end to verify the function's correctness.