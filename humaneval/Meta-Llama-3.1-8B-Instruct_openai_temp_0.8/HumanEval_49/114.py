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
    # Use the built-in pow function with three arguments to compute the power modulo p efficiently
    # This avoids potential overflow errors when dealing with large numbers
    return pow(2, n, p)
```

This script defines a function `modp` that computes `2^n modulo p` using Python's built-in `pow` function with three arguments. The `pow` function first calculates `2^n`, then takes the result modulo `p`, which avoids potential overflow errors when dealing with large numbers. The function includes a docstring that describes its behavior and provides examples for usage.