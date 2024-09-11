Here's a Python script that uses the built-in `pow` function to calculate the modulus in an efficient manner:

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the built-in pow function with three arguments to efficiently
    calculate the modulus in a way that avoids potential overflow issues.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script uses the `pow` function with three arguments to efficiently compute the modulus. The third argument to `pow` is the modulus, which allows it to work efficiently even for large exponents and moduli. This approach avoids potential overflow issues and is generally more efficient than calculating the modulus manually.