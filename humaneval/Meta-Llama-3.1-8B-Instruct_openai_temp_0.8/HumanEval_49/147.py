```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    return pow(2, n, p)
```

This script uses the built-in `pow` function, which takes three arguments: the base, the exponent, and the modulus. It returns the result of the exponentiation modulo the modulus, which is what we want for this problem.

You can use this function as shown in the docstring, for example:

```python
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))   # Output: 2
print(modp(0, 101))   # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))   # Output: 1
```