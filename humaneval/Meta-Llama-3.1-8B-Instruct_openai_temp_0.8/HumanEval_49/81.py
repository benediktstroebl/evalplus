```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    # Use built-in pow function to compute 2^n modulo p efficiently
    # The third argument is the modulus, which avoids large intermediate results
    return pow(2, n, p)


# Test cases
print(modp(3, 5))           # 3
print(modp(1101, 101))     # 2
print(modp(0, 101))        # 1
print(modp(3, 11))         # 8
print(modp(100, 101))      # 1
```

This script uses the built-in `pow` function in Python, which can compute the power operation (`x^n`) with a specified modulus (`m`). The `pow(x, n, m)` function returns `x^n % m`, which is exactly what we need for this problem. This approach is efficient and avoids large intermediate results.