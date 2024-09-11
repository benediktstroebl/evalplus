### Modular Exponentiation
#### Python Implementation

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
    # Use the built-in pow function with three arguments for efficient modular exponentiation
    return pow(2, n, p)
```

You can run this script in your Python environment to test the `modp` function with different inputs. This function takes advantage of Python's built-in support for modular arithmetic in the `pow` function, which is more efficient than manually computing the modular exponentiation.