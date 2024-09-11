### Modular Exponentiation Function
Here's a self-contained Python script that solves the modular exponentiation problem:
```markdown
```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

    Example use cases:
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
    if p == 0:
        raise ValueError("Modulus cannot be zero")
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result
```

You can run the code snippet in a Python environment to test the `modp` function. This function uses the built-in properties of modular arithmetic to efficiently calculate the result of 2^n modulo p. It uses a binary exponentiation approach to reduce the number of multiplications required. Note that the function raises a `ValueError` if the modulus is zero.
```