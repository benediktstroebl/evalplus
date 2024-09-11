```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that
    (a*b) mod n = ((a mod n) * (b mod n)) mod n.

    Args:
        n (int): The base number.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
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

This script defines a function `modp(n, p)` that calculates `2^n modulo p`. It uses a loop to repeatedly multiply the result by 2, taking the modulus `p` at each step. This approach avoids potential overflow issues that could arise from computing `2^n` directly for large values of `n`. The function includes docstrings to explain its purpose, behavior, and input/output parameters. The script also includes test cases to verify the function's correctness.