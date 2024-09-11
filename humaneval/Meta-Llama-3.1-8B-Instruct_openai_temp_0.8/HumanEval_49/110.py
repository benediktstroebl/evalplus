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


# Example usage:
if __name__ == "__main__":
    print(modp(3, 5))    # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))   # 1
    print(modp(3, 11))    # 8
    print(modp(100, 101))  # 1
```

This Python script defines a function `modp(n, p)` that calculates 2^n modulo p using the built-in `pow()` function, which supports three arguments: `base`, `exponent`, and `modulus`. This is more efficient and numerically stable than recalculating the power and then taking the modulus. The example usage at the end demonstrates how to use this function.