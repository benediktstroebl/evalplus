```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Args:
        n (int): The exponent.
        p (int): The modulus.

    Returns:
        int: The result of 2^n modulo p.
    """
    # Handle edge cases where n is 0 or negative, since 2^0 and 2^-n are 1 and 2^n mod p respectively
    if n == 0:
        return 1
    elif n < 0:
        return modp(-n, p) if p!= 2 else 0  # 2^-n is 0 when p is 2, but 2^0 is 1 when p is 2

    # Use the property of modular exponentiation: (a*b) mod n = ((a mod n) * (b mod n)) mod n
    # to avoid large intermediate results
    result = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        n //= 2
        base = (base * base) % p

    return result

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
```

This code uses the property of modular exponentiation to avoid large intermediate results. It calculates 2^n mod p by iteratively squaring the base (2 mod p) and reducing the exponent (n) by half, until the exponent becomes 0. The result is the final value of the result variable. 

This approach ensures that the result is calculated modulo p at each step, which prevents the buildup of large intermediate results. This makes the code efficient for large inputs. 

Note that the code also handles edge cases where n is 0 or negative, since 2^0 and 2^-n are 1 and 2^n mod p respectively.