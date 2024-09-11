```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    if n == 0:
        return 1
    if n % 2 == 0:
        half = modp(n // 2, p)
        return (half * half) % p
    else:
        return (2 * modp(n - 1, p)) % p

# Test cases
print(modp(3, 5))       # 3
print(modp(1101, 101)) # 2
print(modp(0, 101))    # 1
print(modp(3, 11))     # 8
print(modp(100, 101))  # 1
```

This Python script implements a recursive function `modp` that calculates `2^n modulo p`. If `n` is 0, the function returns 1, as any number to the power of 0 is 1. If `n` is even, the function calculates `2^n modulo p` as `(2^(n/2) modulo p)^2 modulo p`. If `n` is odd, the function calculates `2^n modulo p` as `(2 * (2^(n-1) modulo p) modulo p)`. The function uses the property of modular arithmetic that `(a * b) mod n = ((a mod n) * (b mod n)) mod n`. The test cases are included at the end of the script to verify the correctness of the `modp` function.