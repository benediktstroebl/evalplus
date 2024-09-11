```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power to which 2 should be raised.
    p (int): The modulo number.

    Returns:
    int: The result of 2^n modulo p.
    """
    # Use built-in pow function to calculate 2^n modulo p
    # This function uses the "Exponentiation by squaring" algorithm for efficiency
    return pow(2, n, p)

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

In this script, I've used the built-in `pow` function in Python, which calculates the power of a number modulo another number. This is more efficient than using the `**` operator to calculate the power and then taking the modulo, especially for large numbers. The `pow` function uses the "Exponentiation by squaring" algorithm, which is a mathematical optimization technique that reduces the number of multiplications required to calculate the power.