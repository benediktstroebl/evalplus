```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.

    Examples:
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
    result = 1  # Initialize result to 1
    base = 2  # The base is 2
    while n > 0:  # Continue until n is 0
        if n % 2 == 1:  # If n is odd
            result = (result * base) % p  # Multiply result by base and take modulo p
        base = (base ** 2) % p  # Square base and take modulo p
        n //= 2  # Divide n by 2
    return result  # Return the final result

# Test the function
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p using exponentiation by squaring, which is a fast and efficient method for computing powers in modular arithmetic. The function takes two integer arguments `n` and `p` and returns the result of the calculation. The function includes docstrings that describe its purpose, usage, and examples of usage. The script also includes a test section where it calls the `modp()` function with various input values to verify its correctness.