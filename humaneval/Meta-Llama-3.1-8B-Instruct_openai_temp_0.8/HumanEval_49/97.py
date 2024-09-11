```python
def modp(n: int, p: int):
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
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This Python script defines a function `modp(n, p)` that calculates `2^n modulo p` using the built-in `pow` function with three arguments, which computes the first argument raised to the power of the second argument modulo the third argument.

The script includes the provided docstring and test cases to ensure the function works as expected. The `doctest` module is used to automatically test the function with the provided test cases.