### Modular Exponentiation using Python
#### Fast Computation of 2^n Modulo p

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
    # Handle the case where p is 1
    if p == 1:
        return 0
    # Initialize result to 1
    result = 1
    # Update x if it is more than or
    # equal to p, to avoid overflow and precision issues
    x = 2 % p
    while n > 0:
        # If n is odd, multiply x with result
        if n % 2 == 1:
            result = (result * x) % p
        # n must be even now
        n = n >> 1 # n = n/2
        # x = x^2
        x = (x * x) % p
    return result

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

**Note:** This implementation uses the property of modular arithmetic that `(a*b) mod n = ((a mod n) * (b mod n)) mod n`. This allows us to compute `2^n mod p` more efficiently by avoiding large intermediate results.