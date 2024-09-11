```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The base number.
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
    # Use the built-in pow function to compute 2^n modulo p efficiently
    return pow(2, n, p)


# Test cases
print(modp(3, 5))  
print(modp(1101, 101))
print(modp(0, 101))
print(modp(3, 11))
print(modp(100, 101))
```

This script uses the `pow` function with three arguments to efficiently compute the modulus `2^n modulo p`. The `pow` function is available in Python 3.2 and later. If you are using an earlier version of Python, you can use the following alternative implementation:

```python
def modp(n: int, p: int):
    res = 1
    for _ in range(n):
        res = (res * 2) % p
    return res
```