```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    Args:
    n (int): The exponent.
    p (int): The modulus.
    
    Returns:
    int: 2^n modulo p.
    
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
    return pow(2, n, p)


# Test cases
print(modp(3, 5))
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))
```

This script defines a function `modp(n, p)` which uses the built-in `pow` function with three arguments to efficiently calculate `2^n modulo p`. The `pow` function with three arguments calculates `x` raised to the power `y` modulo `p` with a much faster time complexity than the naive approach of multiplication.