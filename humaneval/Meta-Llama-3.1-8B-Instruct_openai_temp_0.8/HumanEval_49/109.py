```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a*b) mod p = ((a mod p) * (b mod p)) mod p.
    We take advantage of this property to prevent large numbers from being calculated, which can cause numerical issues.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    result = 1
    base = 2 % p  # Initialize the base as 2 modulo p
    while n > 0:
        # If n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # Square the base and divide n by 2
        base = (base * base) % p
        n = n // 2
    return result

# Test cases
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

This script defines a function `modp(n, p)` that calculates 2^n modulo p using the property of modular arithmetic mentioned above. It then tests this function with the provided test cases. The function uses a while loop to repeatedly square the base and reduce the exponent by half until the exponent is zero. At each step, it checks if the exponent is odd and if so, multiplies the result by the base. The result is then calculated modulo p at each step to prevent large numbers from being calculated.