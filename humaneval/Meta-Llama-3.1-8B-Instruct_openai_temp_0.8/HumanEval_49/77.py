**Modular Exponentiation Using Python**
=====================================

This Python script uses the built-in `pow` function to efficiently compute modular exponentiation.

```markdown
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
        n (int): The exponent.
        p (int): The modulus.
    
    Returns:
        int: The result of 2^n modulo p.
    
    Example Use Cases:
    
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
    return pow(2, n, p)


# Testing the function
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```

**Note:** This script leverages the `pow` function's ability to compute modular exponentiation efficiently using the `x, n, m` form, where `x` is the base, `n` is the exponent, and `m` is the modulus.

In the example usage, we test the `modp` function with various inputs to demonstrate its correctness and efficiency.