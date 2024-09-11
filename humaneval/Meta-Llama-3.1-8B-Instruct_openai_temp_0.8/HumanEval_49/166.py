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
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test the function
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that calculates 2^n modulo p using a loop to avoid potential overflow issues. The function takes two arguments, `n` and `p`, and returns the result of the calculation.

The script also includes test cases to demonstrate the function's behavior.