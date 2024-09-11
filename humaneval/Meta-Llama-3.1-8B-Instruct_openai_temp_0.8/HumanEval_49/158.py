```python
def modp(n: int, p: int) -> int:
    """Return 2^n modulo p (be aware of numerics).
    
    This function uses the property of modular arithmetic that 
    (a * b) % p = ((a % p) * (b % p)) % p, and the fact that 
    2^0 is 1.

    Args:
    n (int): The exponent.
    p (int): The modulus.

    Returns:
    int: 2^n modulo p.
    """
    result = 1
    base = 2 % p  # reducing the base modulo p
    while n > 0:
        # if n is odd, multiply the result by the base
        if n % 2 == 1:
            result = (result * base) % p
        # divide n by 2
        n = n // 2
        # reduce the base modulo p
        base = (base * base) % p
    return result

# Test cases
print(modp(3, 5)) # 3
print(modp(1101, 101)) # 2
print(modp(0, 101)) # 1
print(modp(3, 11)) # 8
print(modp(100, 101)) # 1
```

This script defines the `modp` function, which calculates 2^n modulo p efficiently by using the property of modular arithmetic and a while loop to reduce the exponent. It then tests the function with the provided test cases.