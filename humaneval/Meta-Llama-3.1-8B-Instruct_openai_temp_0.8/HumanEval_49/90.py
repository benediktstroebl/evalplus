```python
def modp(n: int, p: int):
    """
    Return 2^n modulo p (be aware of numerics).

    This function calculates 2^n modulo p, which is useful for avoiding large exponentiation results.
    The result will always be in the range [0, p).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2
    while n > 0:
        # If n is odd, multiply the result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script uses the property of modular arithmetic that `(a * b) % p = ((a % p) * (b % p)) % p`. By using this property, we can avoid large intermediate results and reduce the risk of integer overflows. The script iteratively squares the base and reduces it modulo p, allowing us to compute 2^n modulo p efficiently.