Here's a Python script that uses the built-in `pow` function to efficiently calculate `2^n modulo p`:
```markdown
### modp.py

```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

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

# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This script uses the `pow` function with three arguments: `base`, `exponent`, and `modulus`. This is a more efficient way to calculate `2^n modulo p` because it avoids unnecessary multiplications and uses the property of modular arithmetic that `(a*b) mod n = ((a mod n) * (b mod n)) mod n`.

The script includes doctest to ensure that the function behaves as expected for various inputs.
```
```