```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    This function uses the property of modular arithmetic that (a*b) % n = ((a % n) * (b % n)) % n
    to efficiently compute 2^n modulo p.

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: 2^n modulo p.
    """
    # Initialize result to 1 (since any number to the power of 0 is 1)
    result = 1
    # For each bit in n, if the bit is 1, multiply the result by 2 modulo p
    for bit in bin(n)[2:]:  # Convert n to binary string, remove '0b' prefix
        result = (result * 2) % p  # Multiply result by 2 modulo p
        if bit == '1':  # If current bit is 1
            result = (result * 2) % p  # Multiply result by 2 modulo p
    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This script defines the `modp` function, which efficiently computes 2^n modulo p using the property of modular arithmetic and bitwise operations. It then tests the function with the provided test cases.