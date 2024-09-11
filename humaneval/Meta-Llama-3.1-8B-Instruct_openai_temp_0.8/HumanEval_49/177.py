```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Parameters:
    n (int): The exponent to which 2 should be raised.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This Python script defines a function `modp` that computes `2^n modulo p` using modular exponentiation. It first initializes a result variable to 1 and then iteratively multiplies the result by 2 modulo `p` `n` times. Finally, it returns the result. The test cases are included to demonstrate the function's correctness.