```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).
    
    :param n: The exponent.
    :param p: The modulus.
    :return: 2^n modulo p.
    """
    result = 1
    base = 2 % p  # precalculate 2 mod p to avoid large intermediate results
    
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        n = n >> 1  # divide n by 2
        base = (base * base) % p  # squared base for next iteration
        
    return result

# Example usage:
if __name__ == "__main__":
    print(modp(3, 5))  # 3
    print(modp(1101, 101))  # 2
    print(modp(0, 101))  # 1
    print(modp(3, 11))  # 8
    print(modp(100, 101))  # 1
```

This script includes the `modp` function with documentation and example usage. It uses the property of modular exponentiation, where `(a*b) mod n = ((a mod n) * (b mod n)) mod n`. This helps to avoid large intermediate results and makes the calculation more efficient.