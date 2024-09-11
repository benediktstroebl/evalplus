**Modular Exponentiation**
==========================

Here is a Python script that uses the built-in `pow` function with three arguments to calculate the modular exponentiation efficiently.

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


# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that takes two arguments, `n` and `p`, and returns `2^n modulo p`. The `pow` function is used with three arguments to calculate the modular exponentiation efficiently. The test cases at the end are used to verify the correctness of the function.