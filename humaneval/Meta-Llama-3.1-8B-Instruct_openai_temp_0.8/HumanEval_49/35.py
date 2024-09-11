```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    This function uses the built-in pow() function in Python, which can efficiently
    calculate the power of a number modulo another number, avoiding large intermediate results.

    Args:
        n (int): The exponent.
        p (int): The base and modulus.

    Returns:
        int: 2^n modulo p.
    """
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p using the `pow()` function, which is more efficient than calculating the full power and then taking the modulus. The test cases at the end demonstrate the function's correctness.