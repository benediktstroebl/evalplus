### Modular Exponentiation
#### Using the Built-in `pow` Function with Three Arguments

In Python, the `pow` function can be used to compute modular exponentiation efficiently. It supports three arguments: the base, the exponent, and the modulus.

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
    return pow(2, n, p)


# Example usage:
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This implementation takes advantage of the `pow` function's ability to compute modular exponentiation in constant time, making it efficient for large inputs.