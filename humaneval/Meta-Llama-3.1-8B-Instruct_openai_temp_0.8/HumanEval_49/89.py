### Fast Modular Exponentiation with Built-in Functions
#### Using `pow()` function with `mod` parameter

Here's a Python function that uses the built-in `pow()` function to efficiently compute `(2^n) % p`:

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
    return pow(2, n, p)
```

This function works by using `pow()` with two additional arguments: `n` and `p`. The `pow()` function will compute `2 ^ n` and then return the result modulo `p`, avoiding potential overflow issues.

This solution is efficient because `pow()` uses the "exponentiation by squaring" algorithm under the hood, which has a time complexity of O(log n), making it much faster than a naive approach that uses repeated multiplication.