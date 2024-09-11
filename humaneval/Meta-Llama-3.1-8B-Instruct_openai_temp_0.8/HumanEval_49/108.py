```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    :param n: The exponent.
    :param p: The modulus.
    :return: 2^n modulo p.
    """
    result = 1
    for _ in range(n):
        result = (result * 2) % p
    return result

# Test cases
print(modp(3, 5))   # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))   # Output: 8
print(modp(100, 101))  # Output: 1
```

This script defines a function `modp(n, p)` that calculates `2^n modulo p`. It uses a loop to repeatedly multiply the result by 2 and take the modulus `p` to avoid large numbers. The test cases at the end demonstrate the function's correctness.