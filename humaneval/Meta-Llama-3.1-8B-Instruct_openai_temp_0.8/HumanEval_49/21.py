```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The power to which 2 is raised.
    p (int): The modulo value.

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
    # Initialize result to 1
    result = 1
    
    # Update a using the power operator (**)
    # The modulo operation is performed at each step to prevent large numbers
    for _ in range(n):
        result = (result * 2) % p
    
    return result
```

This script provides a function `modp(n, p)` that calculates 2^n modulo p. It uses a for loop to iteratively multiply the result by 2 and take the modulo p at each step, which prevents the result from becoming too large. The script also includes docstrings to provide documentation and example usage.