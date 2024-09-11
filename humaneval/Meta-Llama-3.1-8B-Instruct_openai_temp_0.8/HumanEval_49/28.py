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
    # Use the built-in pow function with three arguments to calculate the power modulo p
    # This is more efficient and numerically stable than calculating the power first and then taking the modulo
    return pow(2, n, p)


# Example usage:
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script uses the `pow` function with three arguments: `a`, `b`, and `c`. The `pow` function is overloaded to return `(a**b) % c`, which makes it more efficient and numerically stable to calculate powers modulo a number.