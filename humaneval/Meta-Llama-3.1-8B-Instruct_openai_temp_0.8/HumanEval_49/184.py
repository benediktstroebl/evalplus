```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulo value.

    Returns:
        int: 2^n modulo p.

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

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp(n, p)` that uses the built-in `pow` function to calculate the result of `2^n modulo p`. The `pow` function can take three arguments: the base, the exponent, and the modulo value. If the modulo value is provided, the result will be the base raised to the power of the exponent modulo the modulo value. This is exactly what we need for this problem. 

The script then includes the same test cases as the original problem to verify the correctness of the function.