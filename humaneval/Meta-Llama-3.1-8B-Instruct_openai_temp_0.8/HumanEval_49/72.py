```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.

    Example:
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

    # Use the built-in pow function with three arguments to compute the power modulo p
    # This is more efficient than computing the power and then taking the modulo
    result = pow(2, n, p)
    
    return result
```

This script uses Python's built-in `pow` function with three arguments to efficiently compute the power modulo `p`. The `pow` function first computes the power and then takes the modulo, which is more efficient than computing the power and then taking the modulo.