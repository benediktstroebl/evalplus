```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    return pow(2, n, p)


# Test the function
import doctest

doctest.testmod(name="modp", verbose=True)
```

This script uses the built-in `pow` function in Python, which has the ability to compute the power modulo `p`, which is exactly what we need for this problem. The `pow(a, b, c)` function computes `a` to the power of `b` and returns the result modulo `c`. In our case, `a` is `2`, `b` is `n`, and `c` is `p`.