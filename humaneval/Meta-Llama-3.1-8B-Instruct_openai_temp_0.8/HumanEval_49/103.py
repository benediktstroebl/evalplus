```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a*b) mod n = ((a mod n) * (b mod n)) mod n.
    By iteratively squaring 2 modulo p, we can calculate 2^n modulo p efficiently.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1  # Initialize result to 1
    base = 2  # Initialize base to 2
    while n > 0:
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square base and divide n by 2
        base = (base * base) % p
        n = n // 2  # Use integer division to avoid floating point results
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines a function `modp` that calculates 2^n modulo p using the property of modular arithmetic mentioned above. The function iteratively squares 2 modulo p and multiplies the result by 2 if n is odd. The test cases at the end demonstrate the function's correctness.