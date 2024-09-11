```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular exponentiation that
    a^(b+c) mod p = (a^b mod p * a^c mod p) mod p

    Args:
        n (int): The power to which 2 should be raised.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1  # Initialize result to 1
    base = 2    # The base is 2
    while n > 0:
        # If n is odd, multiply result by base
        if n % 2 == 1:
            result = (result * base) % p
        # Square base and divide n by 2
        base = (base * base) % p
        n = n // 2  # Perform integer division to avoid float
    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101)) # 1
```

This script uses the property of modular exponentiation to efficiently compute the result. It iteratively squares the base and divides the exponent by 2, while keeping track of the result. The test cases at the end verify the correctness of the implementation.