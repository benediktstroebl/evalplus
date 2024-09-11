### Modular Exponentiation
#### Using Python's Built-in `pow` Function

Here's a Python function that calculates `2^n mod p` efficiently using the built-in `pow` function with three arguments. The `pow(a, b, c)` function returns `a` raised to the power of `b` modulo `c`.

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
```

This function uses the property of modular arithmetic that `(a * b) mod n = ((a mod n) * (b mod n)) mod n`. The `pow` function takes care of this automatically.