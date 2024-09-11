```python
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    The function uses the property of modular arithmetic that states:
    a (mod p) * b (mod p) ≡ ab (mod p).

    This property allows us to compute the power without having to
    store large intermediate results.

    :param n: The exponent
    :param p: The modulus
    :return: 2^n modulo p
    """
    result = 1  # Initialize the result to 1
    base = 2  # Initialize the base to 2

    # Compute the power modulo p using the property of modular arithmetic
    while n > 0:
        if n % 2 == 1:  # If the current bit is 1
            result = (result * base) % p  # Multiply the result by the base modulo p
        n = n >> 1  # Right shift the exponent by 1 bit
        base = (base * base) % p  # Update the base by squaring it modulo p

    return result

# Test cases
print(modp(3, 5))   # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))   # 8
print(modp(100, 101))  # 1
```

This script uses a variation of exponentiation by squaring to compute `2^n modulo p` without having to store large intermediate results. The time complexity of this algorithm is O(log n) due to the use of bitwise right shift to divide the exponent by 2 in each iteration.