```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    The function uses the built-in pow function with three arguments to calculate 
    the power of 2 modulo p. This approach avoids large intermediate results and 
    potential numerical overflow issues.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)

# Test cases
print(modp(3, 5))   # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This Python script defines a function `modp` that calculates `2^n` modulo `p` using the built-in `pow` function with three arguments. The first argument is the base (2), the second is the exponent (`n`), and the third is the modulus (`p`). This approach is more efficient and avoids potential numerical overflow issues compared to manual implementation using loops. The script includes test cases to demonstrate the function's correctness.