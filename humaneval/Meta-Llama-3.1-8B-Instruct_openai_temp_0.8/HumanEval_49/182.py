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
    # Use the built-in pow function with three arguments to efficiently calculate the power and modulus at the same time
    return pow(2, n, p)

# Test cases
print(modp(3, 5))       # 3
print(modp(1101, 101)) # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p efficiently using the `pow` function with three arguments. The `pow` function is a built-in Python function that can calculate the power of a number with a specified modulus. This approach is much faster and more memory-efficient than calculating the power first and then taking the modulus, especially for large inputs.